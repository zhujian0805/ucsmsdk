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

# This script associates a service profile via UCS Manager Methods.
# Usage: associateSPUsingMethods.py [options]
#
# Options:
# -h, --help            show this help message and exit
# -i IP, --ip=IP        [Mandatory] UCSM IP Address
# -u USERNAME, --username=USERNAME
#                       [Mandatory] Account Username for UCSM Login
# -p PASSWORD, --password=PASSWORD
#                       [Mandatory] Account Password for UCSM Login
#
# NOTE: Please make sure sp, spDn and bladeDn should exist in UCS Manager 
# before executing script.

import getpass
import optparse
import platform
from UcsSdk import *
from UcsSdk.MoMeta.OrgOrg import OrgOrg
from UcsSdk.MoMeta.LsServer import LsServer
from UcsSdk.MoMeta.LsBinding import LsBinding
import xml.dom.minidom

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

		sp = "sp_name"
		spDn = "org-root/ls-sp_name"
		bladeDn = "sys/chassis-1/blade-1"

		obj = LsServer()
		obj.setattr(LsServer.DN, spDn)
		obj.setattr(LsServer.NAME, sp)
		obj.setattr(LsServer.STATUS, Status.MODIFIED)

		bindObj = LsBinding()
		bindObj.setattr(LsBinding.PN_DN, bladeDn)
		bindObj.setattr(LsBinding.RN, LsBinding().MakeRn())
		obj.AddChild(bindObj)

		inConfig = ConfigConfig()
		inConfig.AddChild(obj)

		ccm = handle.ConfigConfMo(obj.Dn, inConfig)
		if ccm.errorCode == 0:
			moList = []
			for child in ccm.OutConfig.GetChild():
				moList.append(child)
			WriteObject(moList)
		else:
			WriteUcsWarning('[Error]: ConfigConfMo [Code]:' + ccm.errorCode
						 + ' [Description]:' + ccm.errorDescr)

		handle.Logout()

	except Exception, err:
		handle.Logout()
		print "Exception:", str(err)
		import traceback, sys
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60
