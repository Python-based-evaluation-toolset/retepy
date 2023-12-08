# Retepy - revert template on python

It is difficult to collect information from raw result of evaluation
without a proper automatic scripts.
This project is proposed as a simple framework to support that task.
Moreover, to support graph drawing, the ETL data from raw should be table-liked.

Then if considering revert template as procedure box,
the input are data raw file and a guider template
while the output will be table liked result
(could be CSV or dictionary in python).

The raw processing should be balanced between
the flexible of template extraction and the simple of feature implementation.
Moreover, it is important to note that
none aggregation action should be involved in data extraction.

From our perspective, the raw data is combination of text lines in single file.
Each line consists of one or many useful information in term of subtext.
Therefore, the extract process could start with
a template line that match to multiple raw data lines.
Each template line consist of matching pattern and catching variable.
Matching pattern is used to detect expected line in raw
while catching pattern is special subtext hold expected information.

A template file is combine of 2 parts: header and body.
The header defines table schema including variable name and type.
The body is multiple template lines which is used to capture information
from the raw data.

The parsing process, therefore, is a subset of scanning process
where each data line is parsed through chain of filters
to capture useful information.
Moreover, because a table could have multiple rows,
there need be some special mechanism to detect start and end of row.
Hence, beside of filter to collect information,
there are special filters to record the deliminator of row
which is placed as first and last pattern line in filter chain.
However, the implementation of special filter should be vary
depending on real scenarios.

## Quickstart

Prepare table schema and filter chain.
Table schema is a dictionary with key is column name
and value is column type following python type.
Filter chain is a list of pattern following python **re** module.
```python
header = {
    "demo_subject": str,
    "demo_verb": str,
    "demo_object": str,
    "demo_nb": int,
}

filter_chain = [
    "START",
    "(?P<demo_subject>\w+) (?P<demo_verb>\w+) (?P<demo_object>\w+) .*",
    ".*(?P<demo_nb>\d+).*",
    "END",
]
```

Import, create and configure filter object in order to parse data.
```python
import retepy

filter = retepy.Filter()
filter.head_set(header)
filter.filter_set(filter_chain)
```

The filter has a special configuration to handle
the distribution of parsed data to row in result table called "delim_set"
In the interface, we could enable/disable "start" and "end" delimiter.
If the start option is True,
the first text passed to filter need to match the first filter in chain
in order to create new row, else the filter raise Error of not row available.
The False start option automatically create new row
to hold parsed info if needed.
On the other hand, the end option set to True close current row
on the text matched last filter of filter chain.
The next parsing text will be written to new created row.
False option does not close current row
and the whole parsed info is updated to current row only.
```python
# interface
## filter.delim_set(start:bool=None, end:bool=None)
## Example of enable delimiter
filter.delim_set(True, True)
```

To explain concept of delimiter, we consider filter object as a state machine
holding a row of result table as it's state.
There are three action possible relating to row state:
Creating and jump to new row (1), modifying info of current row (2),
and closing current row and jump to non row state (3).
The **delim_set** interface allows to activate action (1) and (3)
based on text parsed while action (2) is fired in default.
Detail action of (1) (2) are explained above.

Finally, we feed text data to filter to complete information of table
and get out result table.
```
# Simple case
## Row 1
filter.parse("START")
filter.parse("This is demo filter: 1")
filter.parse(". is not valid string 2")
filter.parse("END")

# Multiple row
## Row 2
filter.parse("START")
filter.parse("This is demo filter: 3")
filter.parse("END")

## Row 3
filter.parse("START")
filter.parse("This is demo filter: 4")
filter.parse("END")

# Invalid pass
filter.parse("This is a valid string end: 1")

# Result table
table = filter.table_get()
```
