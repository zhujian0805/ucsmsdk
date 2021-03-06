"""This module contains the meta information of ApeSetServerLifeCycle ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("ApeSetServerLifeCycle", "apeSetServerLifeCycle", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_fru_model": MethodPropertyMeta("InFruModel", "inFruModel", "Xs:string", "Version142b", "Input", False),
    "in_fru_serial": MethodPropertyMeta("InFruSerial", "inFruSerial", "Xs:string", "Version142b", "Input", False),
    "in_fru_vendor": MethodPropertyMeta("InFruVendor", "inFruVendor", "Xs:string", "Version142b", "Input", False),
    "in_server_lc": MethodPropertyMeta("InServerLc", "inServerLc", "Xs:string", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
    "inFruModel": "in_fru_model",
    "inFruSerial": "in_fru_serial",
    "inFruVendor": "in_fru_vendor",
    "inServerLc": "in_server_lc",
}

