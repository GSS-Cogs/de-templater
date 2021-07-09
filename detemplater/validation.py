from enum import Enum

from detemplater.models import DbParadime


# Link "should_match" entries from the journey to any representative enums.
enum_dict = {
    "DbParadime": DbParadime
}


# Where a validation step is configured (i.e "should_match") confirm the declared Enum matches the input as stated
# Note: this is a precaution as using complex strings for control flow without vaidation is a bad idea
def validate_step(step_dict: dict, enum_dict: Enum = enum_dict):
    should_match = step_dict.get("should_match", None)
    if should_match:

        # If we've declarted validation, confirm we have something to validate against.
        if should_match not in enum_dict:
            raise ValueError(f'''Aborting, invalid question. You\'ve declared the choices for the question 
                '{step_dict["name"]} should match the choices declated via the "{should_match}" but no
                enum odf that name exists. This is a coding error.''')

        expected_text_fields = [x.value for x in enum_dict[step_dict["should_match"]]]
        actual_text_fields = [x["text"] for x in step_dict["choices"].values()]

        # TODO - probably should be a comprehension.
        valid = True
        for etf in expected_text_fields:
            if etf not in actual_text_fields:
                valid = False

        if len(expected_text_fields) != len(actual_text_fields):
            valid = False

        if not valid:
            joined_actual_text_fields = "\n".join(expected_text_fields)
            joined_expected_text_fields = "\n".join(actual_text_fields)

            raise ValueError(f'''
            The step [step_dict["name"]] has unexpected inputs defined.

            Expected:
            {joined_expected_text_fields}

            Got:
            {joined_actual_text_fields}
            ''')

    return step_dict
