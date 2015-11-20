"""This module contains the general information for ComputeChassisDiscPolicy ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ComputeChassisDiscPolicyConsts():
    ACTION_1_LINK = "1-link"
    ACTION_2_LINK = "2-link"
    ACTION_4_LINK = "4-link"
    ACTION_8_LINK = "8-link"
    ACTION_IMMEDIATE = "immediate"
    ACTION_PLATFORM_MAX = "platform-max"
    ACTION_USER_ACKNOWLEDGED = "user-acknowledged"
    INT_ID_NONE = "none"
    LINK_AGGREGATION_PREF_NONE = "none"
    LINK_AGGREGATION_PREF_PORT_CHANNEL = "port-channel"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    REBALANCE_IMMEDIATE = "immediate"
    REBALANCE_USER_ACKNOWLEDGED = "user-acknowledged"


class ComputeChassisDiscPolicy(ManagedObject):
    """This is ComputeChassisDiscPolicy class."""

    consts = ComputeChassisDiscPolicyConsts()
    naming_props = set([])

    mo_meta = MoMeta("ComputeChassisDiscPolicy", "computeChassisDiscPolicy", "chassis-discovery", VersionMeta.Version101e, "InputOutput", 0x3ffL, [], ["admin", "pn-policy"], [u'orgOrg'], [], ["Get", "Set"])

    prop_meta = {
        "action": MoPropertyMeta("action", "action", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["1-link", "2-link", "4-link", "8-link", "immediate", "platform-max", "user-acknowledged"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "link_aggregation_pref": MoPropertyMeta("link_aggregation_pref", "linkAggregationPref", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["none", "port-channel"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "qualifier": MoPropertyMeta("qualifier", "qualifier", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, """[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rebalance": MoPropertyMeta("rebalance", "rebalance", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["immediate", "user-acknowledged"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x100L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "action": "action", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "linkAggregationPref": "link_aggregation_pref", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "qualifier": "qualifier", 
        "rebalance": "rebalance", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.action = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.link_aggregation_pref = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.qualifier = None
        self.rebalance = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ComputeChassisDiscPolicy", parent_mo_or_dn, **kwargs)
