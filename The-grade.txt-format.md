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

All lines in a grade.txt file are *single observations about a particular student* or they are definitions of types or instances of observations.  Fields in a given line are separated by semicolons.  The first entry of a line/record indicates the entry type, for example:  id for information about a student (email address, section, demographics, etc.); "att" for a daily attendance entry; "hw" to define the parameters of a homework assignment; "hw-score" to give a student's results on a homework assignment; "quiz" to define the parameters of a quiz or other assessment (ie date, which standards were assessed, etc.); "quiz-score" to give a student's results on a quiz assessment; "standard" to define a skill/goal to be assessed in the course.

Within each line/record, after the entry type, will be a list of key:value pairs, separated by semicolons, giving the appropriate entry parameters. Most entries will have a date:date_val pair, most will have a name:name_val pair.



For example:
<pre>
id; name:Einstein, Albert; section:A; gender:M
att; date:12/02/2013; name:Einstein, Albert; present:1
att; date:12/03/2013; name:Einstein, Albert; present:0
quiz; date:12/03/2013; quiz-name:Quiz 2; quiz-type:[all,makeup,retake]; skill:C1; skill:M2; skill:T3
quiz-score; date:12/03/2013; quiz-name:Quiz 2; name:Einstein, Albert; skill:C1; score:3
quiz-score; date:12/03/2013; quiz-name:Quiz 2; name:Einstein, Albert; skill:M2; score:1
quiz-score; date:12/03/2013; quiz-name:Quiz 2; name:Einstein, Albert; skill:T3; score:4
standard; skill:C1; description:"Communicating results using a graph"
standard; skill:M2; description:"Constructing a model given relevant data"
standard; skill:T3; description:"Identifying relevant variables in constructing an experiment"
hw; date:12/10/2013; hw-id:notes2; scorepossible:5; description:"Notes for Winter Week 2"
hw-score; hw-id:notes2; name:Einstein, Albert; score:5
</pre>




