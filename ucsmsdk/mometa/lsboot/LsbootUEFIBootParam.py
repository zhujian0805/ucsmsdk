"""This module contains the general information for LsbootUEFIBootParam ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LsbootUEFIBootParamConsts():
    pass


class LsbootUEFIBootParam(ManagedObject):
    """This is LsbootUEFIBootParam class."""

    consts = LsbootUEFIBootParamConsts()
    naming_props = set([])

    mo_meta = MoMeta("LsbootUEFIBootParam", "lsbootUEFIBootParam", "uefi-boot-param", VersionMeta.Version224b, "InputOutput", 0xffL, [], ["admin", "ls-config-policy", "ls-server-policy", "ls-storage-policy"], [u'lsbootIScsiImagePath', u'lsbootLanImagePath', u'lsbootLocalHddImage', u'lsbootLocalLunImagePath', u'lsbootSanCatSanImagePath', u'lsbootSanImagePath'], [], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "boot_description": MoPropertyMeta("boot_description", "bootDescription", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x2L, 0, 510, None, [], []), 
        "boot_loader_name": MoPropertyMeta("boot_loader_name", "bootLoaderName", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], []), 
        "boot_loader_path": MoPropertyMeta("boot_loader_path", "bootLoaderPath", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version224b, MoPropertyMeta.INTERNAL, 0x10L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x20L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, 0x40L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x80L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "bootDescription": "boot_description", 
        "bootLoaderName": "boot_loader_name", 
        "bootLoaderPath": "boot_loader_path", 
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.boot_description = None
        self.boot_loader_name = None
        self.boot_loader_path = None
        self.child_action = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LsbootUEFIBootParam", parent_mo_or_dn, **kwargs)

