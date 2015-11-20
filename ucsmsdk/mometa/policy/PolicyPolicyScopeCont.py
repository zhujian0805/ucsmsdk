"""This module contains the general information for PolicyPolicyScopeCont ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class PolicyPolicyScopeContConsts():
    NEED_RECOVERY_FALSE = "false"
    NEED_RECOVERY_NO = "no"
    NEED_RECOVERY_TRUE = "true"
    NEED_RECOVERY_YES = "yes"


class PolicyPolicyScopeCont(ManagedObject):
    """This is PolicyPolicyScopeCont class."""

    consts = PolicyPolicyScopeContConsts()
    naming_props = set([u'appType'])

    mo_meta = MoMeta("PolicyPolicyScopeCont", "policyPolicyScopeCont", "scope-cont-[app_type]", VersionMeta.Version211a, "InputOutput", 0x1fL, [], ["admin"], [u'extpolClient', u'extpolController', u'extpolProvider', u'extpolRegistry', u'policyPolicyEp'], [u'policyPolicyScopeContext'], [None])

    prop_meta = {
        "app_type": MoPropertyMeta("app_type", "appType", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x1L, 1, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "gen_num": MoPropertyMeta("gen_num", "genNum", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "need_recovery": MoPropertyMeta("need_recovery", "needRecovery", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "appType": "app_type", 
        "childAction": "child_action", 
        "dn": "dn", 
        "genNum": "gen_num", 
        "needRecovery": "need_recovery", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, app_type, **kwargs):
        self._dirty_mask = 0
        self.app_type = app_type
        self.child_action = None
        self.gen_num = None
        self.need_recovery = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "PolicyPolicyScopeCont", parent_mo_or_dn, **kwargs)
