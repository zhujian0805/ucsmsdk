"""This module contains the meta information of MethodVessel ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("MethodVessel", "methodVessel", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "in_stimuli": MethodPropertyMeta("InStimuli", "inStimuli", "MethodSet", "Version142b", "Input", True),
}

prop_map = {
    "cookie": "cookie",
    "inStimuli": "in_stimuli",
}

