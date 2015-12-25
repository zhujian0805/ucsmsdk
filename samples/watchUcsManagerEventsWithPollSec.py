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

# This script monitors the UCS Manager events after every PollSec.
# Usage: watchUcsManagerEventsWithPollSec.py [options]
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
from UcsSdk.MoMeta.LsServer import LsServer

def getpassword(prompt):
	if platform.system() == "Linux":
		return getpass.unix_getpass(prompt=prompt)
	elif platform.system() == "Windows" or platform.system() == "Microsoft":
		return getpass.win_getpass(prompt=prompt)
	else:
		return getpass.getpass(prompt=prompt)

def calback_pollSec(mce):
	print 'Received Service Profile Event of classId: ' + str(mce.mo.classId)
	print 'Value of Property USR_LBL: ' + mce.mo.UsrLbl
	print "ChangeList: ", mce.changeList

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

		SP = handle.GetManagedObject(None, LsServer.ClassId(), 
							{LsServer.DN:"org-root/ls-ServiceProfileName"})
		
		# Add an event handle to catch the event triggered by "Change in Value 
		# of any of the specific Property of the respective Managed Object".
		# Using PollSec, will poll for specifc event after every pollSec.
		
		# NOTE: Once an event is received, event handle will be automatically 
		# removed.
		ev_pollSec= handle.AddEventHandler(managedObject = SP[0], 
					prop = NamingPropertyId.USR_LBL, successValue=["Success"],
					 pollSec=20, callBack=calback_pollSec)
		
		# loop that keeps the script running for us to get events/callbacks
		# User needs to manually exit the script here.
		while True:
			time.sleep(5)
		
		handle.Logout()
	
	except Exception, err:
		handle.Logout()
		print "Exception:", str(err)
		import traceback, sys
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60
		
