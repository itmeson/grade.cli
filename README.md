grade.txt-cli
=========

A command-line grade entry tool.  Partially inspired by todo.sh and standards based grading.

Every new piece of information about a student will be entered as a single line in a text file, using key:value
pairs to indicate the meaning of entries, in much the same way that todo.sh uses priorities, contexts, and projects
to slice the todo.txt file into useful subsets.

A companion tool (or tools) will parse the grade.txt file, preparing reports for students and teacher, and 
using pandas for exploratory data analysis on the student records.

Key features (for me) for the cli is that it be very fast to enter student notes, comments, scores, attendance, etc.
without the overheard of alphabetizing stacks of papers, finding columns or rows in spreadsheets, insuring that 
consistency of naming is maintained, or waiting on a web interface.

For the analysis and reporting tool, the key feature is that it be very simple and fast to enter desired slices,
and that it be simple to build standard queries and reports that can be updated as data are entered using the
cli.

It seems that much of the cli could be written as a variant of the todo.txt-cli, but I would rather work in python
for now.

License:
--------

MIT License

Copyright 2013, Mark Betnel.
