

STANDARD_IMPORTS = """# ## Imports and Basic Classes
#
# Note: If you need to access the contents of `info.json` at any point in your transform there's no need to open it again, it's already available at `metadata.seed`.

from gssutils import *
cubes = Cubes("info.json")
"""

REUSABLE_FUNCTIONS = """
# ### Reusable Functions
#
# If you're defining functions for use anywhere in the notebook, put them here. For some guidance, please see [reusable functions](https://github.com/GSS-Cogs/de-templater/tree/main/detemplater/docs/functions.md)

# +
# Please include a doc string explaining the purpose of any functions as well as type hints.
# -
"""

SELECTING_SOURCE_DATA_FUNCTIONS_NO_CATALOG = """
# ### Functions To Select Source Data

# +
def get_metadata():
    metadata = Scraper(seed="info.json")
    return metadata  

def select_distribution(metadata):
    return metadata.distribution(latest=True)
# -
"""

SELECTING_SOURCE_DATA_FUNCTIONS_WITH_CATALOG = """
# ### Functions To Select Source Data
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

DATABAKER_ITERATE_TO_SINGLE_OUTPUT = """

# ### Un-pivot the data
# This stage should be getting the spreadsheet of data into one or more pandas dataframes.
# Any interventions to modify those dataframes shoud happen in section **3. Post Processing**.
#
# _Note: You can access the name of any given tab in the loop via `tab.name`._
#
# For some examples, see [Databaker Basics](https://github.com/GSS-Cogs/de-templater/tree/main/detemplater/docs/databaker.md)

# +

extracted_tabs_as_dataframes = []

# Loop through databaker tabs.
for tab in distribution.as_databaker():

    observations = 

    area = 

    period = 

    # HDim() or HDimConst()
    dimensions = [
        
    ]

    cs = ConverstionSegment(tab, observations, dimensions)
    # savepreviewhtml(cs)
    df = cs.topandas()

    extracted_tabs_as_dataframes.append(df)

df = pd.concat(extracted_tabs_as_dataframes)

# -
"""

DATABAKER_ITERATE_TO_MULTIPLE_OUTPUTS_COMMENT = """
# ### Define lists of tabs (with each list eventually being joined to form a single output)
#
# **Important**, please do a replace of the below (output_1, output_2) to something a bit more descriptive of your transform. To replace in a Jupyter notebook hit cmd+f then the small down arrow next to the find box to replace.
"""

DATABAKER_ITERATE_TO_MULTIPLE_OUTPUTS = """
output_{}_df_list = []
"""

DATABAKER_ITERATE_TO_MULTIPLE_OUTPUTS_LOOP = """
# ### Creating output_{i}_df

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
    # savepreviewhtml(cs)
    df = cs.topandas()

    output_{i}_df_list.append(df)

output_{i}_df = pd.concat(output_{i}_df_list)

# Post Professing

# output_{i}_df =
# output_{i}_df =
# output_{i}_df =

cubes.add_cube(distribution, df, "<TITLE GOES HERE / distribution.title>")
# -
"""

DATABAKER_SELECT_BY_TAB_NAME_START = """

all_tabs_dict = {tab.name: tab for tab in distribution.as_databaker()}
"""

DATABAKER_EACH_SELECT_BY_TAB_NAME = """

df = None
while not df:

    tab = all_tabs_dict["<PUT NAME OF TAB HERE>"]
    print(f'Processing tab {tab.name}')

    observations = 

    area = 

    period = 

    # HDim() or HDimConst()
    dimensions = [
        
    ]

    cs = ConverstionSegment(tab, observations, dimensions)
    # savepreviewhtml(cs)
    df = cs.topandas()

    # Post processing for this tab

    # Output this tab
    cubes.add_cube(distribution, df, "<TITLE GOES HERE / distribution.title>")
"""

SINGLE_OUTPUT_POST_PROCESSING_AND_WRITE = """
# ### Post Processing & Write
# Any chances **after** the source data is in a tidy (one observation per row) format should be done here.
# For some examples, see [Post Processing Basics](https://github.com/GSS-Cogs/de-templater/tree/main/detemplater/docs/postprocessing.md)

# +

# Post Proccessing
# df = <whatever>


# Output
cubes.add_cube(distribution, df, "<TITLE GOES HERE / distribution.title>")
cubes.output_all()
# -
"""

CUBES_OUTPUT_ALL = """
cubes.output_all()
"""

SIMPLE_PANDAS_TRANSFORM = """
df = distribution.as_pandas()

# Post processing

# Output
cubes.add_cube(distribution, df, "<TITLE GOES HERE / distribution.title>")
cubes.output_all()
"""