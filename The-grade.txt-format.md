The grade.txt Format
====================
A complete primer on the whys and hows of grade.txt

Why plain text?
===============
Plain text is software and operating system agnostic. It’s searchable, portable, lightweight and easily manipulated. It’s unstructured. It works when someone else’s web server is down or your Outlook .PST file is corrupt. There’s no exporting and importing, no databases or tags or flags or stars or prioritizing or [Insert company name here]-induced rules on what you can and can’t do with it.

The axes of an effective grade book
===================================

Using special notation in grade.txt, you can create a list of observations
about your students that are sliceable by _x_ axes.

*Name* most importantly, you want to be able to easily find all observations about a given student

*Observation type* you want to be able to aggregate narrative comments, homework assignments, assessment results, attendance, etc.

*Standard* you want to be able to find observations indexed by the relevant learning standard 

*Documentation* if there is a relevant documentation file (sample of student work, for example), you want to be able to find it

*Date* you want to be able find and order things by date submitted, date due, etc.

The format
==========

All lines in a grade.txt file are *single observations about a particular student* or they are definitions of types or instances of observations, with all data entries in a line given in key:value pairs.

For example:

 @ date:2013-11-24 name:"Albert Einstein" quiz:"Quiz 10 Newton's 2nd Law" "R evience":3 "M acceleration":2 @
 @ date:2013-11-24 quiz:"Quiz 10 Newton's 2nd Law" skill:"R evidence" skill:"M acceleration" @
 @ skill:"R evidence" description:"I am able to evaluate the meaning of evidence about a phenomenon in order to draw conclusions about explanations of that phenomenon, using data provided in the form of tables, graphs, and narrative observations." @

define a relevant skill, a quiz that assesses that skill, and a particular student's results on that quiz.

 @ date:2013-11-24 name:"Albert Einstein" attendance:present@
 @ date:2013-11-24 name:"Max Planck" attendance:absent@

detail student attendance.





