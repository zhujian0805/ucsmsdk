"""This module contains the general information for LstorageLunReplicationTask ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LstorageLunReplicationTaskConsts():
    pass


class LstorageLunReplicationTask(ManagedObject):
    """This is LstorageLunReplicationTask class."""

    consts = LstorageLunReplicationTaskConsts()
    naming_props = set([])

    mo_meta = MoMeta("LstorageLunReplicationTask", "lstorageLunReplicationTask", "lun-repl-task", VersionMeta.Version302c, "InputOutput", 0x3fL, [], ["admin", "ls-storage", "ls-storage-policy"], [u'lstorageLunReplicationPolicy'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "volume_name": MoPropertyMeta("volume_name", "volumeName", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "volumeName": "volume_name", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.sacl = None
        self.status = None
        self.volume_name = None

        ManagedObject.__init__(self, "LstorageLunReplicationTask", parent_mo_or_dn, **kwargs)

