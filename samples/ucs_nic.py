#!/usr/bin/python
#coding: utf-8
"""Get the Serial Numbers for Blades, Rack Servers, Fabric Interconnnects,
    and IOMs"""

from UcsSdk.UcsHandle import UcsHandle
from UcsSdk.MoMeta.ComputeBlade import ComputeBlade
from UcsSdk.MoMeta.EquipmentChassis import EquipmentChassis
from UcsSdk.MoMeta.ComputeRackUnit import ComputeRackUnit
from UcsSdk.MoMeta.NetworkElement import NetworkElement
#from UcsSdk.MoMeta.EquipmentFex import  EquipmentFex
from UcsSdk.MoMeta.EquipmentIOCard import  EquipmentIOCard
from UcsSdk.MoMeta.EquipmentSwitchCard import  EquipmentSwitchCard
from UcsSdk.MoMeta.VnicEther import VnicEther

import csv
import argparse
from pprint import pprint

CONST_DEBUG = False
CONST_HEADER_ROW = (('EQUIPMENTTYPE', 'EQUIPMENTID', 'SERIALNUMBER'))


def main(args):
    """Main Function, open a file, write to it"""

    handle = UcsHandle()
    handle.Login(args.ucs)

    # Get all Nics
    nic_list = handle.GetManagedObject(None, VnicEther.ClassId(), None,
                                       dumpXml=CONST_DEBUG)

    for nic in nic_list:
        pprint(('NIC', nic.Addr, nic.Dn))

    handle.Logout()

if __name__ == '__main__':

    PARSER = argparse.ArgumentParser(description="Dump Serial Numbers to CSV")
    PARSER.add_argument('-u', '--ucs', help="UCS Manager IP", required=True)

    ARGS = PARSER.parse_args()
    main(ARGS)

