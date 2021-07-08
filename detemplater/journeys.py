
# TODO: via yaml would be more readable
ALL_JOURNEYS = {
  "journeys": {
    "v1_basic": {
      "0": {
        "id": "is_catalog",
        "name": "Is the resource dataset part of a catalog?",
        "choices": {
          "1": {
            "text": "Yes"
          },
          "2": {
            "text": "No"
          },
          "3": {
            "text": "Use gssutils to check if metadata is a catalog",
            "investigate": True
          }
        }
      },
      "1": {
        "id": "file_type",
        "name": "What input file format will you be working with?",
        "choices": {
          "1": {
            "text": "xls"
          },
          "2": {
            "text": "xlsx"
          },
          "3": {
            "text": "ods"
          },
          "4": {
            "text": "csv",
            "pops": [
              "databaker_paradime",
              "how_many_individual_tab_selections"
            ]
          }
        },
        "guidance": [
          "extract"
        ]
      },
      "2": {
        "id": "databaker_paradime",
        "name": "Which best describes how you are using databaker?",
        "should_match": "DbParadime",
        "choices": {
          "1": {
            "text": "You want to iterate through the tabs, joining them into a SINGLE output",
            "pops": [
              "how_many_individual_tab_selections",
              "how_many_individual_outputs"
            ]
          },
          "2": {
            "text": "You want to iterate through the tabs, joining them to create MULTIPLE outputs",
            "pops": [
              "how_many_individual_tab_selections"
            ]
          },
          "3": {
            "text": "Select by name: You want to select individual tab(s) by name and process them without a loop.",
            "pops": [
              "how_many_individual_outputs"
            ]
          }
        }
      },
      "3": {
        "id": "how_many_individual_tab_selections",
        "name": "How many individual tab selections are you going to start with? (if its more than three this is probably the wrong approach)",
        "choices": {
          "1": {
            "text": 1
          },
          "2": {
            "text": 2
          },
          "3": {
            "text": 3
          }
        }
      },
      "4": {
        "id": "how_many_individual_outputs",
        "name": "How many individual outputs are you expecting to create from this sheet?",
        "choices": {
          "1": {
            "text": 1
          },
          "2": {
            "text": 2
          },
          "3": {
            "text": 3
          },
          "4": {
            "text": 4
          }
        }
      }
    }
  }
}