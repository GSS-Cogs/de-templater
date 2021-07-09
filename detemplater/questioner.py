import json

from detemplater.decisions import Decision
from detemplater.results import Results
from detemplater.investigation import investigate
from detemplater.allquestions import QUESTION_SUITES

class Questioner:
    """
    The class that guides the user through the defined journey,
    collecting user inputs and managing which steps will and will
    not be shown based on those inputs.
    """

    def __init__(self, info_json_dict: dict = None, question_suite : str = 'v1_basic'):
        self.completed_run: bool = False
        self.step_counter: int = 0
        self.invalidated_steps: list = []
        self.info_json_dict:dict = info_json_dict
        self.results: Results = Results()
        self.question_series: dict = QUESTION_SUITES[question_suite]


    def _get_index_from_name(self, step_id: str):
        """
        Given the name of a step, acquire the index
        of that step from the base journey
        """

        for index, step_dict in self.base_journey.items():
            if step_dict["id"] == step_id:
                return index
        else:
            raise ValueError(f'Could not find a step named {step_id}')


    def next_question(self):
        """
        Ask the next question.

        Note: a question will be skipped if it's index (its number as defined
        in the question suite) appears in self.invalidated_steps.
        """
        decided = False

        while not decided:

            if self.step_counter == len(self.question_series):
                self.completed_run = True
                return None

            decision_dict = self.question_series[self.step_counter]

            if self.step_counter not in self.invalidated_steps:
                decided = True
            
            self.step_counter += 1

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
