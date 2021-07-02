
import json

from gssutils import Scraper

def investigate(info_json_dict: dict, decision_dict: dict):
    """
    Simple function to conditionally acquire extra information for the user
    on request.
    """

    # For is_catalog, we can be asked to Scrape
    if decision_dict["text"] == "Use gssutils to check if metadata is a catalog":
        if not info_json_dict:
            raise ValueError('To request additional information via a scrape'
                ' you must have provided an info.json file.')

        metadata = Scraper(info_json_dict["landingPage"])
        if hasattr(metadata, "datasets"):
            print(f'\nINVESTIGATED: This appears to be a catalog of {len(metadata.datasets)} datasets.\n')
        else:
            print(f'\nINVESTIGATED: This appears to be a simple dataset (so NOT part of a catalog).\n')

    else:
        raise Exception(f'got decision dict {json.dumps(decision_dict, indent=2)}')
 