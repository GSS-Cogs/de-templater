
from typing import Optional
from snippets import (
    STANDARD_IMPORTS,
    REUSABLE_FUNCTIONS,
    SELECTING_SOURCE_DATA_FUNCTIONS_NO_CATALOG,
    INSTANTIATE_SCRAPER,
    SELECT_DISTRIBUTION
    )

class Results:

    def __init__(self):
        # On instantiation, compare with the id in journey.yaml
        # blow up if someoners declaring a non existant id
        self.file_type: Optional[str] = None
        self.iterating_databaker_tabs: Optional[bool] = None

    def output_template(self, file_name: str = "template.py"):

        # TODO - assign logical building blocks based on resultds attributes
        with open(file_name, "w") as f:
            f.write(f"""
            {STANDARD_IMPORTS}
            {REUSABLE_FUNCTIONS}
            {SELECTING_SOURCE_DATA_FUNCTIONS_NO_CATALOG}
            {INSTANTIATE_SCRAPER}
            {SELECT_DISTRIBUTION}
            """.strip()
            )