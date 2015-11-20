"""This module contains the general information for LsbootLanImagePath ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LsbootLanImagePathConsts():
    TARGET_MANAGED = "managed"
    TARGET_UNMANAGED = "unmanaged"
    TARGET_UNSPECIFIED = "unspecified"
    TYPE_PRIMARY = "primary"
    TYPE_SECONDARY = "secondary"


class LsbootLanImagePath(ManagedObject):
    """This is LsbootLanImagePath class."""

    consts = LsbootLanImagePathConsts()
    naming_props = set([u'type'])

    mo_meta = MoMeta("LsbootLanImagePath", "lsbootLanImagePath", "path-[type]", VersionMeta.Version101e, "InputOutput", 0xfffL, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-policy", "ls-storage", "ls-storage-policy"], [u'lsbootLan'], [u'lsbootUEFIBootParam', u'vnicIpV4StaticAddr'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "boot_ip_policy_name": MoPropertyMeta("boot_ip_policy_name", "bootIpPolicyName", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "i_scsi_vnic_name": MoPropertyMeta("i_scsi_vnic_name", "iSCSIVnicName", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "img_policy_name": MoPropertyMeta("img_policy_name", "imgPolicyName", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], []), 
        "img_sec_policy_name": MoPropertyMeta("img_sec_policy_name", "imgSecPolicyName", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, [], []), 
        "prov_srv_policy_name": MoPropertyMeta("prov_srv_policy_name", "provSrvPolicyName", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x80L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "target": MoPropertyMeta("target", "target", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, ["managed", "unmanaged", "unspecified"], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x400L, None, None, None, ["primary", "secondary"], []), 
        "vnic_name": MoPropertyMeta("vnic_name", "vnicName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
    }

    prop_map = {
        "bootIpPolicyName": "boot_ip_policy_name", 
        "childAction": "child_action", 
        "dn": "dn", 
        "iSCSIVnicName": "i_scsi_vnic_name", 
        "imgPolicyName": "img_policy_name", 
        "imgSecPolicyName": "img_sec_policy_name", 
        "provSrvPolicyName": "prov_srv_policy_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "target": "target", 
        "type": "type", 
        "vnicName": "vnic_name", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.boot_ip_policy_name = None
        self.child_action = None
        self.i_scsi_vnic_name = None
        self.img_policy_name = None
        self.img_sec_policy_name = None
        self.prov_srv_policy_name = None
        self.sacl = None
        self.status = None
        self.target = None
        self.vnic_name = None

        ManagedObject.__init__(self, "LsbootLanImagePath", parent_mo_or_dn, **kwargs)
