"""This module contains the general information for ComputeConstraintDef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ComputeConstraintDefConsts():
    CONSTRAINT_TYPE_ADAPTOR = "adaptor"
    CONSTRAINT_TYPE_DIMM = "dimm"
    CONSTRAINT_TYPE_LOCAL_DISK = "local-disk"
    CONSTRAINT_TYPE_UNKNOWN = "unknown"
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class ComputeConstraintDef(ManagedObject):
    """This is ComputeConstraintDef class."""

    consts = ComputeConstraintDefConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("ComputeConstraintDef", "computeConstraintDef", "cons-def-[name]", VersionMeta.Version302a, "InputOutput", 0x7fL, [], [""], [u'equipmentBladeCapProvider', u'equipmentRackUnitCapProvider'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "constraint_type": MoPropertyMeta("constraint_type", "constraintType", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["adaptor", "dimm", "local-disk", "unknown"], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "hw_model": MoPropertyMeta("hw_model", "hwModel", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "hw_revision": MoPropertyMeta("hw_revision", "hwRevision", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "hw_vendor": MoPropertyMeta("hw_vendor", "hwVendor", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version302a, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302a, MoPropertyMeta.NAMING, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "constraintType": "constraint_type", 
        "descr": "descr", 
        "dn": "dn", 
        "hwModel": "hw_model", 
        "hwRevision": "hw_revision", 
        "hwVendor": "hw_vendor", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.constraint_type = None
        self.descr = None
        self.hw_model = None
        self.hw_revision = None
        self.hw_vendor = None
        self.int_id = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "ComputeConstraintDef", parent_mo_or_dn, **kwargs)
