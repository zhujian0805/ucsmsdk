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

# This script will sync the organisation between two UCS Manager.
# Scenario:
# Both UCS Manager contains organisation "TestSyncOrg" under org-root.
# However UCS Manager with handle2 contains service profile "TestSyncSP" 
# under "TestSyncOrg" but no servie profile under UCS Manager with handle1.
#
# Goal is to make both the Organisation same i.e. to copy the service profile 
# from handle2 to handle1.

from UcsSdk import *
from UcsSdk.MoMeta.OrgOrg import OrgOrg

reference_handle_ip = '<UCSM IP Address>'
reference_handle_user = '<Account Username for UCSM Login>'
reference_handle_password = '<Account Password for UCSM Login>'


difference_handle_ip = '<UCSM IP Address>'
difference_handle_user = '<Account Username for UCSM Login>'
difference_handle_password = '<Account Password for UCSM Login>'

try:    
    reference_handle = UcsHandle()
    reference_handle.Login(reference_handle_ip, reference_handle_user, 
                           reference_handle_password)
    
    difference_handle = UcsHandle()
    difference_handle.Login(difference_handle_ip, difference_handle_user, 
                            difference_handle_password)
    
    
    moList1 = reference_handle.GetManagedObject(None, OrgOrg.ClassId(), 
                       {OrgOrg.DN:"org-root/org-TestSyncOrg"}, YesOrNo.TRUE)
    moList2 = difference_handle.GetManagedObject(None, OrgOrg.ClassId(), 
                       {OrgOrg.DN:"org-root/org-TestSyncOrg"}, YesOrNo.TRUE)
 
    # Compare will return a different object either showing sign "=>" means 
    # managed object has to be added to reference object 
    # or sign "<=" means # managed object has to be removed from reference 
    # object.
    modiff = CompareManagedObject(referenceObject=moList1, 
                                  differenceObject=moList2)
    print "\n modiff"
    WriteObject(modiff)

    # Run the sync object on the reference object handle. In this case, 
    # handle1.
    reference_handle.SyncManagedObject(difference=modiff, 
                                       deleteNotPresent=True, dumpXml=False)
    
    reference_handle.Logout()
    difference_handle.Logout()
    
except Exception, err:
    reference_handle.Logout()
    difference_handle.Logout()
    print "Exception:", str(err)
    import traceback, sys
    print '-'*60
    traceback.print_exc(file=sys.stdout)    
    print '-'*60
    
    
