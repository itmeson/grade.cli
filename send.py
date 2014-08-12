import datetime


def send(text, email=None, passfile="pass.dat", test=True, subject="None"):
    """Simple email sender, using a pass.dat file for authentication.
	Defaults to print the message header and output, set test=True
	to send."""
# Import smtplib for the actual sending function
    import smtplib

# Import the email modules we'll need
    from email.mime.text import MIMEText

# Encode the text of the message as MIMEText
    msg = MIMEText(text)

    password, me = getPass(passfile)

    you = email #== the recipient's email address
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


def getPass(passfile="pass.dat"):
# get the sender info from a file  (first line pass, second line email)
    p = open(passfile, 'rU')
    password = p.readline().strip()
    me = p.readline().strip()
    p.close()
    return (password, me)


def sendhtml(text, html, email=None, passfile="pass.dat", test=True, subject="None"):
    import smtplib

    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # me == my email address
    # you == recipient's email address
    password, me = getPass(passfile)
    you = email
# Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Test"
    msg['From'] = me
    msg['To'] = you


# Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    if test:
        print msg.as_string()
        return
# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

# Send the message via local SMTP server.
    s = smtplib.SMTP('smtp.gmail.com', 587)
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
    s.starttls()
    s.login(me, password)
    s.sendmail(me, [you], msg.as_string())
    s.quit()

