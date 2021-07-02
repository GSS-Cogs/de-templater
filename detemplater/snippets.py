

STANDARD_IMPORTS = """# ## 0. Imports and Basic Classes
#
# Note: If you need to access the contents of `info.json` at any point in your transform there's no need to open it again, it's already available at `metadata.seed`.

from gssutils import *
cubes = Cubes("info.json")
"""

REUSABLE_FUNCTIONS = """
# ### Reusable Functions
#
# If you're defining functions for use anywhere in the notebook, put them here.

# +
# Please include a doc string explaining the purpose of any functions as well as type hints.
# -
"""

SELECTING_SOURCE_DATA_FUNCTIONS_NO_CATALOG = """
# ### 1. Functions To Select Source Data

# +
def get_metadata():
    metadata = Scraper(seed="info.json")
    return metadata  

def select_distribution(metadata):
    return metadata.distribution(latest=True)
# -
"""

SELECTING_SOURCE_DATA_FUNCTIONS_WITH_CATALOG = """
# ### 1. Functions To Select Source Data
# For more information on making selections from metadata, please see: [Metadata Selections](https://github.com/GSS-Cogs/de-templater/tree/main/detemplater/docs/metaselections.md)

# +
def get_metadata():
    metadata = Scraper(seed="info.json")
    return metadata  

def select_dataset(metadata):
    metadata.select_dataset(latest=True)
    return metadata

def select_distribution(metadata):
    return metadata.distribution(latest=True)
# -
"""

INSTANTIATE_SCRAPER = """
# #### Instantiate Scraper

# +
metadata = get_metadata()
metadata
# -
"""

SELECT_DATASET = """
# #### Select dataset

# +
metadata = select_dataset(metadata)
metadata
# -
"""

SELECT_DISTRIBUTION = """
# #### Select distribution

# +
distribution = select_distribution(metadata)
distribution
# -
"""

DATABAKER_LOOP = """

# ### 2. Un-pivot the data
#
# _Note: You can access the name of any given tab in the loop, with `tab.name`._

# +

# Loop through databaker tabs.
for tab in distribution.as_databaker():

    observations = 

    area = 

    period = 

    # HDim() or HDimConst()
    dimensions = [
        
    ]

    cs = ConverstionSegment(tab, observations, dimensions)
    df = cs.topandas()

#-
"""
