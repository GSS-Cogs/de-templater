
import json

from detemplater.validation import validate_step 

class Decision:
    """
    An individual decision point.
    """
    def __init__(self, step_dict: dict):
        self.step_dict = validate_step(step_dict)
        self.decision_dict = {}
        self.decision_is = None


    def _present_guidance(self, info_json_dict: dict):
        """
        Prints a little bit of the info.json to help guide
        a user choice.
        """
        if "guidance" in self.step_dict:
            print('The following informations from the info.json '
                'may help with the following question.')
            for related_info_json_field in self.step_dict["guidance"]:
                if isinstance(related_info_json_field, str):
                    print(json.dumps(info_json_dict[related_info_json_field], indent=2))
            print()


    def _present_choices(self):
        """
        Presents the user with the available answer to this question.
        """
        print(self.step_dict["name"], "\n")
        for choice, choice_dict in self.step_dict["choices"].items():
            print(f'{choice}: {choice_dict["text"]}')
            self.decision_dict[str(choice)] = choice_dict
        print()



