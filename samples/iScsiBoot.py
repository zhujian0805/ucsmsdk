#!/usr/bin/python

# Copyright 2013 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This script creates a service profile and configure it to boot from an iSCSI.
# Usage: iScsiBoot.py [options]
#
# Options:
# -h, --help            show this help message and exit
# -i IP, --ip=IP        [Mandatory] UCSM IP Address
# -u USERNAME, --username=USERNAME
#                       [Mandatory] Account Username for UCSM Login
# -p PASSWORD, --password=PASSWORD
#                       [Mandatory] Account Password for UCSM Login
#

import getpass
import optparse
import platform
from UcsSdk import *
from UcsSdk.MoMeta.OrgOrg import OrgOrg
from UcsSdk.MoMeta.LsServer import LsServer
from UcsSdk.MoMeta.VnicEther import VnicEther
from UcsSdk.MoMeta.VnicEtherIf import VnicEtherIf
from UcsSdk.MoMeta.VnicIScsi import VnicIScsi
from UcsSdk.MoMeta.VnicVlan import VnicVlan
from UcsSdk.MoMeta.VnicIPv4If import VnicIPv4If
from UcsSdk.MoMeta.VnicIPv4IscsiAddr import VnicIPv4IscsiAddr
from UcsSdk.MoMeta.VnicIScsiStaticTargetIf import VnicIScsiStaticTargetIf
from UcsSdk.MoMeta.VnicLun import VnicLun
from UcsSdk.MoMeta.LsbootDef import LsbootDef
from UcsSdk.MoMeta.LsbootVirtualMedia import LsbootVirtualMedia
from UcsSdk.MoMeta.LsbootIScsi import LsbootIScsi
from UcsSdk.MoMeta.LsbootIScsiImagePath import LsbootIScsiImagePath

def getpassword(prompt):
	if platform.system() == "Linux":
		return getpass.unix_getpass(prompt=prompt)
	elif platform.system() == "Windows" or platform.system() == "Microsoft":
		return getpass.win_getpass(prompt=prompt)
	else:
		return getpass.getpass(prompt=prompt)

if __name__ == "__main__":
	handle = UcsHandle()
	try:
		parser = optparse.OptionParser()
		parser.add_option('-i', '--ip',dest="ip",
		                  help="[Mandatory] UCSM IP Address")
		parser.add_option('-u', '--username',dest="userName",
		                  help="[Mandatory] Account Username for UCSM Login")
		parser.add_option('-p', '--password',dest="password",
		                  help="[Mandatory] Account Password for UCSM Login")

		(options, args) = parser.parse_args()
		
		if not options.ip:
			parser.print_help()
			parser.error("Provide UCSM IP Address")
		if not options.userName:
			parser.print_help()
			parser.error("Provide UCSM UserName")
		if not options.password:
			options.password=getpassword("UCSM Password:")

		handle.Login(options.ip,options.userName,options.password)
		handle.StartTransaction()

		getRsp = handle.GetManagedObject(None, None,{OrgOrg.DN:"org-root"})
		sp = handle.AddManagedObject(getRsp, LsServer.ClassId(), 
						{LsServer.TYPE:"instance", LsServer.NAME:"sp_name"})
		vnic = handle.AddManagedObject(sp, VnicEther.ClassId(), 
						{VnicEther.NAME:"enic1", VnicEther.SWITCH_ID:"A", 
						VnicEther.ADDR:"00:00:00:22:22:27"})
		vlan611 = handle.AddManagedObject(vnic, VnicEtherIf.ClassId(), 
				{VnicEtherIf.NAME:"vlan611", VnicEtherIf.DEFAULT_NET:"yes"})

		enic = handle.AddManagedObject(sp, VnicIScsi.ClassId(),	
				{VnicIScsi.NAME:"iscsienic1", VnicIScsi.INITIATOR_NAME:
								"iqn.1995-05.com.broadcom.iscsiboot2",
								VnicIScsi.VNIC_NAME:"enic1"})
		vlan = handle.AddManagedObject(enic, VnicVlan.ClassId(), 
									{VnicVlan.VLAN_NAME:"vlan611"})
		ipv4if = handle.AddManagedObject(vlan, VnicIPv4If.ClassId())
		ipv4iscsi = handle.AddManagedObject(ipv4if, VnicIPv4IscsiAddr.ClassId()
									, {VnicIPv4IscsiAddr.ADDR:"10.10.10.10"})

		primaryTarget = handle.AddManagedObject(vlan, 
							VnicIScsiStaticTargetIf.ClassId(), 
							{VnicIScsiStaticTargetIf.IP_ADDRESS:"10.10.10.11", 
		VnicIScsiStaticTargetIf.NAME:"iqn.1992-08.com.netapp:sn.135037408", 
		VnicIScsiStaticTargetIf.PRIORITY:"1"})
		primaryLun = handle.AddManagedObject(primaryTarget, VnicLun.ClassId(), 
											{VnicLun.ID:"2"})

		bootPolicy = handle.AddManagedObject(sp, LsbootDef.ClassId())

		vmedia = handle.AddManagedObject(bootPolicy, 
				LsbootVirtualMedia.ClassId(), {LsbootVirtualMedia.ACCESS:
								"read-only", LsbootVirtualMedia.ORDER:"1"})

		iscsiBoot = handle.AddManagedObject(bootPolicy, LsbootIScsi.ClassId(),
										 {LsbootIScsi.ORDER:"2"})
		iscsiBootImagePath = handle.AddManagedObject(iscsiBoot, 
		LsbootIScsiImagePath.ClassId(), {LsbootIScsiImagePath.TYPE:"primary",
						LsbootIScsiImagePath.I_SCSIVNIC_NAME:"iscsienic1"})

		handle.CompleteTransaction()

		handle.Logout()

	except Exception, err:
		handle.Logout()
		print "Exception:", str(err)
		import traceback, sys
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60
