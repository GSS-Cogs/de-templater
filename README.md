# de-templater

An script that creates standard templates with boilerplate for common data transformation scenarios.

## Install

```
pip install --no-cache git+git://github.com/GSS-Cogs/de-templater.git#egg=detemplater
```

## Usage

The templater is command line callable, so to use:

* Navigate to a directory that contains an info.json file.
* run `detemplate` on the command line.

_Note: It's worth looking through the source file and/or spec a bit before running the templater as it'll ask you a few questions about what you're looking to do._


# Tests

From the root of your clones de-templater repo run `python -m unittest discover -v tests`

Otherwise, tests will trigger when you push changes to a branch as per standard github CI practice (this is powered by the included github action).


# How it works

There's no real decision tree (i.e no branching logic) to this. When you run the templater you select a series of questions defined by a dictionary. The current default dictionary is defined as `v1_basic` from `QUESTION_SUITES` in `detemplater/allquestions.py`.

Each journey consists of multiple questions/steps, with each question step having multiple possible answers referred to as choices.

Every choice has an index number and a text field (the question the user will be asked) and the default choices for the users - as well as a few optional special fields (there are examples of each of these in the default question suite).

* `pops` - a list of identifiers for later questions we wish to remove if a given choice is selected - this gets us primitive control flow.
* `guidance` - fields from info.json we wish to be displayed on screen when the question is asked.
* `should_match` - primitive validation of inputs. This is principally to allow us to handle more complex mutli tiered choices with some assurance that a well intentioned tweak of wording won't spiral into unexpected and hard to debug behaviour (i.e complex conditionals based on unvalidated string content would be asking for trouble). 
* `investigate` - if something is tagged as "investigate" detemplate will expect ad-hoc handling in `investigation.py` to provide additional information to the user.