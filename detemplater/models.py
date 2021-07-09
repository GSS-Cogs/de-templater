
from enum import Enum

# We're gonna use Enums to define more complex choice to make things a bit easier to follow
class DbParadime(Enum):
    iterate_single_output = "You want to iterate through the tabs, joining them into a SINGLE output"
    iterate_multiple_output = "You want to iterate through the tabs, joining them to create MULTIPLE outputs"
    select_by_tab_name = "Select by name: You want to select individual tab(s) by name and process them without a loop."
