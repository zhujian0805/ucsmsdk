"""This module contains the general information for ApeMc ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ApeMcConsts():
    UPDATE_TYPE_DELTA = "delta"
    UPDATE_TYPE_PERIODIC = "periodic"
    UPDATE_TYPE_SYNC = "sync"


class ApeMc(ManagedObject):
    """This is ApeMc class."""

    consts = ApeMcConsts()
    naming_props = set([u'ip'])

    mo_meta = MoMeta("ApeMc", "apeMc", "mc-[ip]", VersionMeta.Version101e, "InputOutput", 0xffL, [], ["read-only"], [u'apeManager'], [u'apeMcTable'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "ip": MoPropertyMeta("ip", "ip", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x8L, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40L, 0, 510, None, [], []), 
        "update_type": MoPropertyMeta("update_type", "updateType", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["delta", "periodic", "sync"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "ip": "ip", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
        "updateType": "update_type", 
    }

    def __init__(self, parent_mo_or_dn, ip, **kwargs):
        self._dirty_mask = 0
        self.ip = ip
        self.child_action = None
        self.sacl = None
        self.status = None
        self.type = None
        self.update_type = None

        ManagedObject.__init__(self, "ApeMc", parent_mo_or_dn, **kwargs)

