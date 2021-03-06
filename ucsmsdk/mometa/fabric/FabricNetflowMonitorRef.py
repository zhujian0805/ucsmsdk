"""This module contains the general information for FabricNetflowMonitorRef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FabricNetflowMonitorRefConsts():
    DIRECTION_RECEIVE = "receive"
    DIRECTION_TRANSMIT = "transmit"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class FabricNetflowMonitorRef(ManagedObject):
    """This is FabricNetflowMonitorRef class."""

    consts = FabricNetflowMonitorRefConsts()
    naming_props = set([u'nfMonitorName', u'direction'])

    mo_meta = MoMeta("FabricNetflowMonitorRef", "fabricNetflowMonitorRef", "flow-monitor-[nf_monitor_name]-dir-[direction]", VersionMeta.Version221b, "InputOutput", 0xffL, [], ["admin", "ext-lan-config", "ext-lan-policy"], [u'fabricNetflowMonSession'], [u'faultInst'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "direction": MoPropertyMeta("direction", "direction", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x4L, None, None, None, ["receive", "transmit"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "index": MoPropertyMeta("index", "index", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], ["0-2"]), 
        "nf_monitor_name": MoPropertyMeta("nf_monitor_name", "nfMonitorName", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x20L, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "oper_nf_monitor_name": MoPropertyMeta("oper_nf_monitor_name", "operNfMonitorName", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x40L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x80L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "direction": "direction", 
        "dn": "dn", 
        "index": "index", 
        "nfMonitorName": "nf_monitor_name", 
        "operNfMonitorName": "oper_nf_monitor_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "switchId": "switch_id", 
    }

    def __init__(self, parent_mo_or_dn, nf_monitor_name, direction, **kwargs):
        self._dirty_mask = 0
        self.nf_monitor_name = nf_monitor_name
        self.direction = direction
        self.child_action = None
        self.index = None
        self.oper_nf_monitor_name = None
        self.sacl = None
        self.status = None
        self.switch_id = None

        ManagedObject.__init__(self, "FabricNetflowMonitorRef", parent_mo_or_dn, **kwargs)

