
from enum import Enum


class Decision:
    """
    An individual decision point.
    """
    def __init__(self, step_dict: dict):
        self.step_dict = step_dict
        self.decision_dict = {}
        self.decision_is = None


    def _present_guidance(self):
        """
        TODO - show whats in the info.json so users get
        some hint as to what the right choice is
        """
        pass

    def _present_choices(self):
        """
        
        """
        print(self.step_dict["name"])
        for choice, choice_dict in self.step_dict["choices"].items():
            print(f'{choice}: {choice_dict["text"]}')
            self.decision_dict[str(choice)] = choice_dict
        print()



