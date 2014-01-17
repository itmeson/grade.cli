def send(text, email="itmeson@gmail.com", test = False, subject="None"):
# Import smtplib for the actual sending function
    import smtplib

# Import the email modules we'll need
    from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
    textfile = "test.dat"
#    fp = open(textfile, 'rb')
# Create a text/plain message
#    text = fp.read()
#    fp.close()
    msg = MIMEText(text)

# get the sender password from a file  (first line pass, second line email)
    p = open('pass.dat', 'rU')
    password = p.readline().strip()
    me = p.readline().strip()
    p.close()


    you = email #"itmeson@gmail.com" #== the recipient's email address
    msg['Subject'] = subject #'The contents of %s' % textfile
    msg['From'] = me
    msg['To'] = you

    if test:
	print msg.as_string()
	return
# Send the message via our own SMTP server, but don't include the
# envelope header.
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(me, password)
    s.sendmail(me, [you], msg.as_string())
    s.quit()



def allQuizScore(g, subject="Recent Scores", test=False):
    names = g.GradeBook.names.keys()
    names.sort()	
    for name in names:
        if 'quizscore' in g.GradeBook.names[name]:
            output = ''
            output += name + '\n\n'
	    quizitems = g.GradeBook.names[name]['quizscore']
	    quizitems.sort()
	    for item in quizitems: 
	        #print "\t\t", item
	        date = item['date']
	        date2 = date[:2] + '.' + date[2:4] + '.' + date[4:]
	        output += date2 + '\t' +  item['quizname'] + '\n'
	        output += 'Skill:\t' + item['skill'] + '\t' 
	        if 'score' in item:
		    output += 'Score:\t' + item['score']
	        output += '\n'
	        if 'comment' in item:
		    output += 'Comment:\t' + item['comment']
                output += "\n\n"

            send(output, g.GradeBook.names[name]['id'][0]['email'], test=test, subject = subject)



import grade as g


#poss = g.GradeBook.possibilities

#for p in poss:
#    print p
#    for item in poss[p]:
#	print item,
#    print "\n\n"


g.GradeBook.parseDATA()

#for name in g.GradeBook.names:
#    print name
#    for item in g.GradeBook.names[name]:
#        print "\t", item
#	for res in g.GradeBook.names[name][item]:
#	    print "\t\t", res
#	print "\n"
#    print "\n\n"


#for t in g.GradeBook.things:
#    print t, '\n\t', g.GradeBook.things[t]


allQuizScore(g, subject="LabScience: Recent score updates", test = True)

