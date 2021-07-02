
from typing import Optional
from snippets import (
    STANDARD_IMPORTS,
    REUSABLE_FUNCTIONS,
    SELECTING_SOURCE_DATA_FUNCTIONS_NO_CATALOG,
    SELECTING_SOURCE_DATA_FUNCTIONS_WITH_CATALOG,
    INSTANTIATE_SCRAPER,
    SELECT_DATASET,
    SELECT_DISTRIBUTION,
    DATABAKER_LOOP
    )

class Results:

    def __init__(self):
        # On instantiation, compare with the id in journey.yaml
        # blow up if someoners declaring a non existant id
        self.is_catalog: Optional[bool] = None
        self.file_type: Optional[str] = None
        self.iterating_databaker_tabs: Optional[bool] = None

    def output_template(self, file_name: str = "template.py"):

        snippets_required = [STANDARD_IMPORTS, REUSABLE_FUNCTIONS]

        if self.is_catalog:
            snippets_required.append(SELECTING_SOURCE_DATA_FUNCTIONS_WITH_CATALOG)
        else:
            snippets_required.append(SELECTING_SOURCE_DATA_FUNCTIONS_NO_CATALOG)
        snippets_required.append(INSTANTIATE_SCRAPER)
        if self.is_catalog:
            snippets_required.append(SELECT_DATASET)
        snippets_required.append(SELECT_DISTRIBUTION)

        if self.iterating_databaker_tabs:
            snippets_required.append(DATABAKER_LOOP)

        # TODO - assign logical building blocks based on resultds attributes
        with open(file_name, "w") as f:
            for snippet in snippets_required:
                f.write(snippet)