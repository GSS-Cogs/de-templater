from enum import Enum
import json

from typing import Union
from decision_tree import DecisionTree

def run(info_json: str = "info.json"):
    with open(info_json, "r") as f:
        info_json_dict = json.load(f)

    decision_tree = DecisionTree(info_json_dict)

    print()
    while decision_tree.walk():
        this_step = decision_tree.next_choice()
        if not this_step:
            break

        this_step._present_guidance(info_json_dict)
        this_step._present_choices()
        decision_tree.make_a_decision(this_step)
        print()

    decision_tree.results.output_template()

run()