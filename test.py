def send():
# Import smtplib for the actual sending function
    import smtplib

# Import the email modules we'll need
    from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
    textfile = "test.dat"
    fp = open(textfile, 'rb')
# Create a text/plain message
    msg = MIMEText(fp.read())
    fp.close()

    me = "mbetnel@seattleacademy.org" #= the sender's email address
    you = "itmeson@gmail.com" #== the recipient's email address
    msg['Subject'] = 'The contents of %s' % textfile
    msg['From'] = me
    msg['To'] = you

# get the password from a file
    p = open('pass.dat', 'rU')
    password = p.readline().strip()
    p.close()

# Send the message via our own SMTP server, but don't include the
# envelope header.
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('mbetnel@seattleacademy.org', password)
    s.sendmail(me, [you], msg.as_string())
    s.quit()


send()
