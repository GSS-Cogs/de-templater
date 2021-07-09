
from gssutils import Scraper

def investigate(info_json_dict: dict, decision_dict: dict):
    """
    Simple function to conditionally acquire extra information for the user
    on request.

    handling is triggered based on the text of the question which is accessible via
    decision dict. If no handlig is triggered we will err at the end (to avoid well 
    intentioned tweaks of wording silently breaking the logic).

    These will typicially be one to one with questions from journey so please
    keep with the convention of commenting the question id above each block of
    logic.
    """

    # is_catalog
    if decision_dict["text"] == "Use gssutils to check if metadata is a catalog":
        if not info_json_dict:
            raise ValueError('To request additional information via a scrape'
                ' you must have provided an info.json file.')

        metadata = Scraper(info_json_dict["landingPage"])
        if hasattr(metadata.catalog, "dataset") > 0:
            print(f'\nINVESTIGATED: This appears to be a catalog of {len(metadata.catalog.dataset)} datasets.\n')
        else:
            print(f'\nINVESTIGATED: This appears to be a simple dataset (so NOT part of a catalog).\n')

    else:
        raise Exception(f'"investigate" keyword provided but no handling detected for this step, '
            f' we we\re expecting handling for question "{decision_dict["text"]}".')
 