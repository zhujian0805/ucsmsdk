"""This module contains the general information for FirmwareActivity ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FirmwareActivityConsts():
    SERVERS_POWER_STATE_NONE = "none"
    SERVERS_POWER_STATE_OFF = "off"
    SERVERS_POWER_STATE_OFF_NOWAIT = "off-nowait"
    SERVERS_POWER_STATE_ON = "on"


class FirmwareActivity(ManagedObject):
    """This is FirmwareActivity class."""

    consts = FirmwareActivityConsts()
    naming_props = set([])

    mo_meta = MoMeta("FirmwareActivity", "firmwareActivity", "fw-activity", VersionMeta.Version251a, "InputOutput", 0xfL, [], ["admin"], [u'equipmentChassis'], [], [None])

    prop_meta = {
        "chassis_comp_in_activation_dn": MoPropertyMeta("chassis_comp_in_activation_dn", "chassisCompInActivationDn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version251a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "server_comp_in_activation_dn": MoPropertyMeta("server_comp_in_activation_dn", "serverCompInActivationDn", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "servers_power_state": MoPropertyMeta("servers_power_state", "serversPowerState", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["none", "off", "off-nowait", "on"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version251a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "upgrade_priority_info": MoPropertyMeta("upgrade_priority_info", "upgradePriorityInfo", "string", VersionMeta.Version251a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|cmc-update|cmc-activate|board-controller|storage-controller|chassis-adaptor-update|chassis-adaptor-activate),){0,6}(none|cmc-update|cmc-activate|board-controller|storage-controller|chassis-adaptor-update|chassis-adaptor-activate){0,1}""", [], []), 
    }

    prop_map = {
        "chassisCompInActivationDn": "chassis_comp_in_activation_dn", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "serverCompInActivationDn": "server_comp_in_activation_dn", 
        "serversPowerState": "servers_power_state", 
        "status": "status", 
        "upgradePriorityInfo": "upgrade_priority_info", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.chassis_comp_in_activation_dn = None
        self.child_action = None
        self.server_comp_in_activation_dn = None
        self.servers_power_state = None
        self.status = None
        self.upgrade_priority_info = None

        ManagedObject.__init__(self, "FirmwareActivity", parent_mo_or_dn, **kwargs)
