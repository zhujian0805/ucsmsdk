"""This module contains the general information for MgmtConnection ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class MgmtConnectionConsts():
    ACK_ACKNOWLEDGED = "acknowledged"
    ACK_UN_INITIALIZED = "un-initialized"
    ACK_UNSUPPORTED_CONNECTIVITY = "unsupported-connectivity"
    OPER_STATE_ACKNOWLEDGED = "acknowledged"
    OPER_STATE_UN_INITIALIZED = "un-initialized"
    OPER_STATE_UNSUPPORTED_CONNECTIVITY = "unsupported-connectivity"
    TYPE_SHARED_LOM = "shared-lom"
    TYPE_SIDEBAND = "sideband"
    TYPE_UNSPECIFIED = "unspecified"


class MgmtConnection(ManagedObject):
    """This is MgmtConnection class."""

    consts = MgmtConnectionConsts()
    naming_props = set([u'type'])

    mo_meta = MoMeta("MgmtConnection", "mgmtConnection", "mgmt-connection-[type]", VersionMeta.Version211a, "InputOutput", 0x7fL, [], ["admin"], [u'mgmtController'], [u'faultInst'], ["Get", "Set"])

    prop_meta = {
        "ack": MoPropertyMeta("ack", "ack", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["acknowledged", "un-initialized", "unsupported-connectivity"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x4L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["acknowledged", "un-initialized", "unsupported-connectivity"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x40L, None, None, None, ["shared-lom", "sideband", "unspecified"], []), 
    }

    prop_map = {
        "ack": "ack", 
        "childAction": "child_action", 
        "dn": "dn", 
        "operState": "oper_state", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.ack = None
        self.child_action = None
        self.oper_state = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "MgmtConnection", parent_mo_or_dn, **kwargs)

