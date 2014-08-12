import report as r
import grade as g
import os

test = False

files = os.listdir('Wmid/')

names = g.GradeBook.names.keys()
names.sort()	

for f in files:
    if f[-3:] == 'rep':
	data = open('Wmid/' + f,'r')
	info = data.readlines()
	name = info[2].strip()
	data.close()
	output = "Dear " + name.split(',')[1] + ',\n'
	output += "\nThis is your midterm comment and grade report.  If you see any errors, please let me know right away so I can fix them before Thursday.  If you would like to improve your grade, let me know and I will help you do that before the end of the winter trimester. \n\n -- Mark \n\n" 
	output += ''.join(info)

        r.send(output, g.GradeBook.names[name]['id'][0]['email'], test=test, subject = "Labscience: Mid-tri progress report")

	
