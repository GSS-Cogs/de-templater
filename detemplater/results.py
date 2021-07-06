
from enum import Enum
from typing import Optional

from detemplater.validation import DbParadime
from detemplater.snippets import (
    STANDARD_IMPORTS,
    REUSABLE_FUNCTIONS,
    SELECTING_SOURCE_DATA_FUNCTIONS_NO_CATALOG,
    SELECTING_SOURCE_DATA_FUNCTIONS_WITH_CATALOG,
    INSTANTIATE_SCRAPER,
    SELECT_DATASET,
    SELECT_DISTRIBUTION,
    DATABAKER_ITERATE_TO_MULTIPLE_OUTPUTS_COMMENT,
    DATABAKER_ITERATE_TO_MULTIPLE_OUTPUTS,
    DATABAKER_ITERATE_TO_MULTIPLE_OUTPUTS_LOOP,
    DATABAKER_ITERATE_TO_SINGLE_OUTPUT,
    DATABAKER_SELECT_BY_TAB_NAME_START,
    DATABAKER_EACH_SELECT_BY_TAB_NAME,
    SINGLE_OUTPUT_POST_PROCESSING_AND_WRITE,
    CUBES_OUTPUT_ALL,
    SIMPLE_PANDAS_TRANSFORM
    )


# We're gonna use Enum to make things a bit easier to follow
class DbParadime(Enum):
    iterate_single_output = "You want to iterate through the tabs, joining them into a SINGLE output"
    iterate_multiple_output = "You want to iterate through the tabs, joining them to create MULTIPLE outputs"
    select_by_tab_name = "Select by name: You want to select individual tab(s) by name and process them without a loop."


class InvalidLogicError(Exception):
    """
    Raised if we've created a combination of decision points that doesn't
    make sense.
    """

    def __init__(self, msg):
        self.msg = msg


class Results:

    def __init__(self):
        self.is_catalog: Optional[bool] = None
        self.file_type: Optional[str] = None
        self.databaker_paradime: Optional[str] = None
        self.how_many_individual_tab_selections: Optional[str] = None
        self.how_many_individual_outputs: Optional[str] = None


    def validate(self):
        """
        Validate the properties. Makes sure there are no combinations of
        attributes that should not exist.

        i.e Built in check that nobody has mangled the journey logic.
        """

        if self.file_type == "csv" and self.databaker_paradime:
            raise InvalidLogicError('You should never be selected a databaker paradime'
                ' for a csv. Your journey logic is wrong.')

        if self.file_type == "csv" and self.how_many_individual_tab_selections:
            raise InvalidLogicError('You should never be selected a number of tabs'
                ' for a csv. Your journey logic is wrong.')


    def output_template(self, file_name: str = "template.py"):

        snippets_required = [STANDARD_IMPORTS, REUSABLE_FUNCTIONS]

        # Input is either a catalog (list) of datasets the DE needs to filter
        # or it's alreadty in the form of a single dataset.
        if self.is_catalog:
            snippets_required.append(SELECTING_SOURCE_DATA_FUNCTIONS_WITH_CATALOG)
        else:
            snippets_required.append(SELECTING_SOURCE_DATA_FUNCTIONS_NO_CATALOG)
        snippets_required.append(INSTANTIATE_SCRAPER)
        if self.is_catalog:
            snippets_required.append(SELECT_DATASET)
        snippets_required.append(SELECT_DISTRIBUTION)

        # If we're using databaker, set up appropriate boilerplate
        if self.databaker_paradime:
            if self.databaker_paradime == DbParadime.iterate_multiple_output.value:
                snippets_required.append(DATABAKER_ITERATE_TO_MULTIPLE_OUTPUTS_COMMENT)

                for i in range(0, int(self.how_many_individual_outputs)):
                    snippets_required.append(DATABAKER_ITERATE_TO_MULTIPLE_OUTPUTS.format(str(i+1)))
                for i in range(0, int(self.how_many_individual_outputs)):
                    snippets_required.append(DATABAKER_ITERATE_TO_MULTIPLE_OUTPUTS_LOOP.format(i=str(i+1)))
                snippets_required.append(CUBES_OUTPUT_ALL)

            elif self.databaker_paradime == DbParadime.iterate_single_output.value:
                snippets_required.append(DATABAKER_ITERATE_TO_SINGLE_OUTPUT)
                snippets_required.append(SINGLE_OUTPUT_POST_PROCESSING_AND_WRITE)

            elif self.databaker_paradime == DbParadime.select_by_tab_name.value:
                snippets_required.append(DATABAKER_SELECT_BY_TAB_NAME_START)
                for _ in range(0, int(self.how_many_individual_tab_selections)):
                    snippets_required.append(DATABAKER_EACH_SELECT_BY_TAB_NAME)
                snippets_required.append(CUBES_OUTPUT_ALL)

            else:
                expected_paradime_choices = "\n".join([x.value for x in DbParadime])
                raise Exception(f'''Unable to find the provided databaker paradime amongst the known options.

Got the option:
{self.databaker_paradime}

Known options:\n
{expected_paradime_choices}
                ''')
        
        # It's a csv, so we're using pandas    
        else:
            snippets_required.append(SIMPLE_PANDAS_TRANSFORM)


        with open(file_name, "w") as f:
            for snippet in snippets_required:
                f.write(snippet)