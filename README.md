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
