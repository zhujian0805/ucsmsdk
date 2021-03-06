"""This module contains the general information for LstorageLocalDiskRef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LstorageLocalDiskRefConsts():
    pass


class LstorageLocalDiskRef(ManagedObject):
    """This is LstorageLocalDiskRef class."""

    consts = LstorageLocalDiskRefConsts()
    naming_props = set([u'enclosureId', u'slotId'])

    mo_meta = MoMeta("LstorageLocalDiskRef", "lstorageLocalDiskRef", "diskref-[enclosure_id]-slot-[slot_id]", VersionMeta.Version251a, "InputOutput", 0x7fL, [], ["read-only"], [], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version251a, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "enclosure_id": MoPropertyMeta("enclosure_id", "enclosureId", "uint", VersionMeta.Version251a, MoPropertyMeta.NAMING, 0x8L, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "slot_id": MoPropertyMeta("slot_id", "slotId", "uint", VersionMeta.Version251a, MoPropertyMeta.NAMING, 0x20L, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "enclosureId": "enclosure_id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "slotId": "slot_id", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, enclosure_id, slot_id, **kwargs):
        self._dirty_mask = 0
        self.enclosure_id = enclosure_id
        self.slot_id = slot_id
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LstorageLocalDiskRef", parent_mo_or_dn, **kwargs)

