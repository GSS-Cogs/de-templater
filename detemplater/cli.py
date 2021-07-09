import json

from detemplater.questioner import Questioner

def run_cli(info_json: str = "info.json"):
    """
    Collect information from the user via multiple choice 
    questons on the command line
    """

    with open(info_json, "r") as f:
        info_json_dict: dict = json.load(f)

    question_asker = Questioner(info_json_dict)

    print()
    while not question_asker.completed_run:
        a_question = question_asker.next_question()
        if not a_question:
            break

        a_question._present_guidance(info_json_dict)
        a_question._present_choices()
        question_asker.make_a_decision(a_question)
        print()

    question_asker.results.output_template()

if __name__ == "__main__":
    run_cli()