"""This module contains the general information for VnicDynamicCon ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class VnicDynamicConConsts():
    DYNAMIC_ETH_OFF = "off"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    PROTECTION_NONE = "none"
    PROTECTION_PROTECTED = "protected"
    PROTECTION_PROTECTED_PREF_A = "protected-pref-a"
    PROTECTION_PROTECTED_PREF_B = "protected-pref-b"


class VnicDynamicCon(ManagedObject):
    """This is VnicDynamicCon class."""

    consts = VnicDynamicConConsts()
    naming_props = set([])

    mo_meta = MoMeta("VnicDynamicCon", "vnicDynamicCon", "dynamic-con", VersionMeta.Version101e, "InputOutput", 0x3ffL, [], ["admin", "ls-compute", "ls-config", "ls-network", "ls-network-policy", "ls-server"], [u'lsServer'], [], ["Get", "Set"])

    prop_meta = {
        "adaptor_profile_name": MoPropertyMeta("adaptor_profile_name", "adaptorProfileName", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "dynamic_eth": MoPropertyMeta("dynamic_eth", "dynamicEth", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["off"], ["0-256"]), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "mtu": MoPropertyMeta("mtu", "mtu", "uint", VersionMeta.Version111j, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1500-9000"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "naming_prefix": MoPropertyMeta("naming_prefix", "namingPrefix", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 16, None, [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "protection": MoPropertyMeta("protection", "protection", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["none", "protected", "protected-pref-a", "protected-pref-b"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x100L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "adaptorProfileName": "adaptor_profile_name", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "dynamicEth": "dynamic_eth", 
        "intId": "int_id", 
        "mtu": "mtu", 
        "name": "name", 
        "namingPrefix": "naming_prefix", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "protection": "protection", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.adaptor_profile_name = None
        self.child_action = None
        self.descr = None
        self.dynamic_eth = None
        self.int_id = None
        self.mtu = None
        self.name = None
        self.naming_prefix = None
        self.policy_level = None
        self.policy_owner = None
        self.protection = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "VnicDynamicCon", parent_mo_or_dn, **kwargs)
