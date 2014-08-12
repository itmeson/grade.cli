import sys
from subprocess import call

f= open(sys.argv[1],'rU')

for line in f:
    data = line.strip().split(',')
    url = data[5]
    a = raw_input(data[0])
    if a == '0':
	continue   
    try:
        call(["open", url])
    except:
	print "Not a good url"
	print data, url

