
# Databaker Basics

## Resources

For a day one introduction to databaker and its usage please see the [databaker-walkthrough](https://github.com/GSS-Cogs/databaker-walkthrough).

## FAQ

### 1. What if I don't wanrt to use all the tabs? (so want to get them out of memory).

Three approaches.

a.) Don't load it. You can pass tab names to the `.as_databaker()` method of gssutils to specify which tabs you want.

This has the smallest resource footprint and is the best choice is viable (if the names are changable or the producer is inconsistent, its not).

```python
for tab in distribution.as_databaker(sheetids=["Sheet 1", "Sheet 2"]):
    # do stuff
```

b.) Conditionally filter out what you need before you begin looping through tabs.

If you are building one big loop for sheets with (more or less) similar handling, this is typically the best option.

```python
tabs = distribution.as_databaker()
tabs_i_want = ["Sheet 1", "Sheet 2"]

# then
tabs = [x for x in tabs if x in tabs_i_want]
# or
tabs = [x for x in tabs if x in tabs_i_want]

assert len(tabs) == len(tabs_we_want), 'missing required tab'
for tab in tabs:
    # do stuff
```

c.) Use se the sheet names to exercise flow control.

This is typically best if the tab extractions are almost but not quite the same.

```python
for tab in distribution.as_databaker():
    if tab.name == "Sheet 1":
        # Operations that only apply to sheet 1

    elif tab.name == "Sheet 2":
        # Operations that only apply to sheet 2

    else: 
        raise ValueError(f'Unexpected tab name {tab.name}')

    # Operations that apply to boths sheets.

```