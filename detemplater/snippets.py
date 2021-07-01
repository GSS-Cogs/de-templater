

STANDARD_IMPORTS = """
# ## 0. Imports and Basic Classes
#
# Note: If you need to access the contents of `info.json` at any point in your transform there's no need to open it again, it's already available at `metadata.seed`.

from gssutils import *
cubes = Cubes("info.json")
"""

REUSABLE_FUNCTIONS = """
# ### 0.1 Reusable Functions
#
# If you're defining functions for use anywhere in the notebook, put them here.

# +
# Please include a doc string explaining the purpose of any functions as well as type hints.
# -
"""

SELECTING_SOURCE_DATA_FUNCTIONS_NO_CATALOG = """
# ### 1. Functions To Select Source Data

# +
def get_scraper():
    metadata = Scraper(seed="info.json")
    return metadata  

def select_distribution(metadata):
    return scraper.distribution(latest=True)
# -
"""

INSTANTIATE_SCRAPER = """
# #### 1.1 Instantiate Scraper

# +

scraper = get_scraper()
scraper

# -
"""

SELECT_DISTRIBUTION = """
# #### 1.2 Select distribution

# +

distribution = get_distribution(scraper)
distribution

# -
"""
