
## Databaker Resources

### Walkthrough
For a day one introduction to databaker and its usage please see the [databaker-walkthrough](https://github.com/GSS-Cogs/databaker-walkthrough).


### Selection Methods
This is an old resource, but has some decent information on selection methods [selection menthods](https://ons-opendata.github.io/databaker_docs/selection.html)


## Best Practice

Quick tips that will always apply.

### 1.) Avoid positional references

If you're coding something like `tab.excel_ref('A3')` you're doing it wrong. A column reference ('tab.excel_ref('B')) is typically ok as columns are rarely subject to change, but row or specific cell (or cell range references) are an anti pattern and should only be used in the event all other options are exhausted. 

In order for transforms to be robust you should always aim to use some variation of conditional logic to select cells (as the conditions can still be true in the event of slight structural adjustments).

This _can_ add unecessary complexity, so to mitigtate that please see the section on the anctor pattern detailed below.


### 2.) Use an anchor pattern

An anchor pattern is a best practice pattern that adds a decent level of rubustness with minimal complexity.

Consider this data:
[[[https://raw.githubusercontent.com/GSS-Cogs/databaker-walkthrough/master/databaker-lab-exercises/images/1.png]]

This is a (non robust) selection pattern.
```python
groups = tab.excel_ref('A').filter('Group').expand(DOWN).is_not_blank()
assets = tab.excel_ref('C5:E5')
names = tab.excel_ref('B5:B13').is_not_blank()
```

This is the same code utilising an anchor pattern.
```python
anchor = tab.excel_ref('A').filter(contains_string("roup")).assert_one()
assets = anchor.expand(RIGHT).is_not_blank()
groups = anchor.expand(DOWN).is_not_blank()
names = anchor.shift(RIGHT).fill(DOWN).is_not_blank()
```

The impact:
* Selecting the anchor will work with inconsistent title casing and regardles of whitespace. It was also let you know immediately id the section fails (i.e if it can't assert one).
* Should the structure change over time, the latter pattern is considerably more likely to work as it's a reasonable assumption that the rows and columns will maintain the same pattern relative to "Group".


### 3.) Use assert_one() whenever you're assuming a selection of one

Any selection you are expecting to select a single cell should always make use of `assert_one()`, this is a huge aid to debugging and maintenance. Note - you do not need to end the command with `assert_one()` for example `tab.filter("Text that should only appear once").assert_one().expand(RIGHT).expand(DOWN)` is perectly valid.

### 4.) Comment your selections

Python is self describing...to a point, but your though processes at the time of writing are not. Any given selection should have a short comment above it explaing what the code is aiming to accomplish. The point being - if (or when) the structure changes then it's **immediately obvious to a fellow engineer** when a given line is no longer fulfiling it's intended purpose. If you don't comment the intention it pretty much guarantees exhaustive future investigation.

examples:
```python

# The anchor cell is the long occurance of the word "Group" in column A
anchor = tab.excel_ref('A').filter(contains_string("roup")).assert_one()

# The names of the band members, are expected in the column to the right (and below) the group names
names = anchor.shift(RIGHT).fill(DOWN).is_not_blank()
```
