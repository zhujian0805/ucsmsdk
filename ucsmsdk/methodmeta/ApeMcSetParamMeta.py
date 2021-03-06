"""This module contains the meta information of ApeMcSetParam ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("ApeMcSetParam", "apeMcSetParam", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_mc_ip": MethodPropertyMeta("InMcIp", "inMcIp", "AddressIPv4", "Version142b", "Input", False),
    "in_param_ids": MethodPropertyMeta("InParamIds", "inParamIds", "IdSet", "Version142b", "Input", True),
    "in_param_vals": MethodPropertyMeta("InParamVals", "inParamVals", "ConfigSet", "Version142b", "Input", True),
}

prop_map = {
    "cookie": "cookie",
    "inMcIp": "in_mc_ip",
    "inParamIds": "in_param_ids",
    "inParamVals": "in_param_vals",
}

