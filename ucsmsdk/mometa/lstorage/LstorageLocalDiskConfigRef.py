"""This module contains the general information for LstorageLocalDiskConfigRef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LstorageLocalDiskConfigRefConsts():
    ROLE_DED_HOT_SPARE = "ded-hot-spare"
    ROLE_GLOB_HOT_SPARE = "glob-hot-spare"
    ROLE_NORMAL = "normal"
    ROLE_UNKNOWN = "unknown"
    SPAN_ID_UNSPECIFIED = "unspecified"


class LstorageLocalDiskConfigRef(ManagedObject):
    """This is LstorageLocalDiskConfigRef class."""

    consts = LstorageLocalDiskConfigRefConsts()
    naming_props = set([u'slotNum'])

    mo_meta = MoMeta("LstorageLocalDiskConfigRef", "lstorageLocalDiskConfigRef", "slot-[slot_num]", VersionMeta.Version224b, "InputOutput", 0xffL, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-storage", "ls-storage-policy"], [u'lstorageDiskGroupConfigDef', u'lstorageDiskGroupConfigPolicy'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224b, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "role": MoPropertyMeta("role", "role", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["ded-hot-spare", "glob-hot-spare", "normal", "unknown"], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "slot_num": MoPropertyMeta("slot_num", "slotNum", "ushort", VersionMeta.Version224b, MoPropertyMeta.NAMING, 0x20L, None, None, None, [], ["1-24", "1-4"]), 
        "span_id": MoPropertyMeta("span_id", "spanId", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["unspecified"], ["0-8"]), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x80L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "role": "role", 
        "sacl": "sacl", 
        "slotNum": "slot_num", 
        "spanId": "span_id", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, slot_num, **kwargs):
        self._dirty_mask = 0
        self.slot_num = slot_num
        self.child_action = None
        self.role = None
        self.sacl = None
        self.span_id = None
        self.status = None

        ManagedObject.__init__(self, "LstorageLocalDiskConfigRef", parent_mo_or_dn, **kwargs)

