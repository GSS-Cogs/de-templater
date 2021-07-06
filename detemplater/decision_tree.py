import json
import os
import yaml

from detemplater.decisions import Decision
from detemplater.results import Results
from detemplater.investigation import investigate


class DecisionTree:
    """
    The class that guides users through the appropriate
    decisions, based on the answers provided thus far.
    """

    def __init__(self, info_json_dict: dict = None, chosen_journey : str = 'v1_basic'):
        self.completed_run = False
        self.step_counter = -1
        self.invalidated_steps = []
        self.info_json_dict = info_json_dict
        self.results = Results()

        this_path = os.path.dirname(os.path.realpath(__file__))
        with open(f'{this_path}/journey.yaml') as f:
            all_journeys = yaml.load(f, Loader=yaml.FullLoader)
            self.base_journey = all_journeys["journeys"][chosen_journey]


    def _get_index_from_name(self, step_id):
        """
        Given the name of a step, acquire the index
        of that step from the base journey
        """

        for index, step_dict in self.base_journey.items():
            if step_dict["id"] == step_id:
                return index
        else:
            raise ValueError(f'Could not find a step named {step_id}')


    def next_choice(self):
        """
        Provide the next decision
        """
        decided = False

        while not decided:

            self.step_counter += 1

            try:
                decision_dict = self.base_journey[self.step_counter]
            except KeyError:
                return None

            if self.step_counter not in self.invalidated_steps:
                decided = True

        return Decision(decision_dict)


    def make_a_decision(self, decision: Decision):

        choice = input("What is your decision.... ")

        if "Y" in decision.step_dict["choices"] and "N" in decision.step_dict["choices"]:
            valid_responses = ["Y", "N"]
            int_or_str = "str"
        else:
            valid_responses = [str(x) for x in decision.step_dict["choices"].keys()]
            int_or_str = "int"

        if choice not in valid_responses:
            print(f'{choice} is not a valid response to this question'
                f' needs to be one of {",".join([str(x) for x in valid_responses])}')
            self.make_a_decision(decision)
        else:

            # Get the original dict defining this choice
            try:
                if int_or_str == "int":
                    decision_dict = decision.step_dict["choices"][int(choice)]
                elif int_or_str == "str":
                    decision_dict = decision.step_dict["choices"][str(choice)]
                else:
                    raise ValueError('Aborting. Choice should have been declared as int or str, '
                        'the fact it has not means there has been a logic error.')

            except KeyError as err:
                raise Exception(f'Dict was {json.dumps(decision.step_dict["choices"], indent=2, default=lambda x: str(x))}') from err

            # Investigate for more information on user request
            if "investigate" in decision_dict:
                investigate(self.info_json_dict, decision_dict)
                self.make_a_decision(decision)

            else:
                # Remove any later steps invalidated by this choice
                if "pops" in decision_dict:
                    unwanted_steps = [decision_dict["pops"]] if not isinstance(decision_dict["pops"], list) \
                        else decision_dict["pops"]
                    for step_id in unwanted_steps:
                        self.invalidated_steps.append(self._get_index_from_name(step_id))

                for attr_k in self.results.__dict__.keys():
                    if attr_k.startswith("_"):
                        continue
                    if attr_k == decision.step_dict["id"]:
                        setattr(self.results, attr_k, decision.decision_dict[str(choice)]["text"])

                print('\n', '-'*30)


    def walk(self):
        return not self.completed_run
