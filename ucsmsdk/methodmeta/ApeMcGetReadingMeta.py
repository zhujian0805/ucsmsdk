"""This module contains the meta information of ApeMcGetReading ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("ApeMcGetReading", "apeMcGetReading", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_mc_ip": MethodPropertyMeta("InMcIp", "inMcIp", "AddressIPv4", "Version142b", "Input", False),
    "in_reading_ids": MethodPropertyMeta("InReadingIds", "inReadingIds", "IdSet", "Version142b", "Input", True),
    "out_reading_vals": MethodPropertyMeta("OutReadingVals", "outReadingVals", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inMcIp": "in_mc_ip",
    "inReadingIds": "in_reading_ids",
    "outReadingVals": "out_reading_vals",
}

