
import datetime
import grade as g
import report as p

g.GradeBook.parseDATA()  # reload data

names = g.GradeBook.names.keys()
names.sort()

hw = g.GradeBook.things['hw']
hw.sort(key=lambda x: datetime.datetime.strptime(x['date'], '%m%d%Y'))

quizzes = g.GradeBook.things['quiz']
quizzes.sort(key = lambda x: datetime.datetime.strptime(x['date'], '%m%d%Y'))

skillIDs = [x['skill'] for x in g.GradeBook.things['standard']]
skillIDs.sort()

summary = open('summary.txt', 'w')

for NAME in names:
    if 'role' in g.GradeBook.names[NAME]['id'][0]:
	continue
    studentRESULTS = {key: [] for key in skillIDs}

    qgrade = [0,0,0.2,0]
    hwgrade = [0,0,0.1,0]
    labgrade = [0,0,0.3,1]
    partgrade = [0,0,0.1,1]
    skillsgrade = [0,0,.3,0]

    print NAME, "\n\n\n", "HOMEWORK", "\n"
    for h in hw:
        print h['date'], h['hwid']
	if 'hwscore' not in g.GradeBook.names[NAME]:
	    break
        for hwscore in g.GradeBook.names[NAME]['hwscore']:
            if hwscore['hwid'] == h['hwid']:
                print "  ", hwscore['score'], "/", h['scorepossible'], hwscore.get('comment','')
                print "\n"
                hwgrade[0] += float(hwscore['score'])/float(h['scorepossible'])
                hwgrade[1] += 1

    hwgrade[3] = hwgrade[0]/hwgrade[1]
    print hwgrade[3]

    print "\n\n\nQUIZZES", "\n"
    for q in quizzes:
        print q['date'], q['quizname']
	if 'quizscore' not in g.GradeBook.names[NAME]:
	    break
        for quizscore in g.GradeBook.names[NAME]['quizscore']:
            if quizscore['quizname'] == q['quizname']:
                print "  ", quizscore['skill'],
                print "  ", quizscore['score'], "/", 4, "\n\t", quizscore.get('comment', '')
                print "\n"
                qgrade[0] += float(quizscore['score'])
                qgrade[1] += 1
                studentRESULTS[quizscore['skill']].append((quizscore['score'], quizscore['date']))
            
            
    qgrade[3] = qgrade[0] / (4*qgrade[1])
    print qgrade[3]

    print "\n\nSKILLS\n"
    for skill in skillIDs:
        skilldata = studentRESULTS[skill]
        if len(skilldata) == 0:
            continue
        skilldata.sort(key = lambda x: datetime.datetime.strptime(x[1], '%m%d%Y'))
        total = 0
        for s in skilldata[:-1]:
            total += float(s[0])
        if len(skilldata) > 1:
            total = 0.4*total/(len(skilldata)-1) + 0.6*float(skilldata[-1][0])
        else:
            total = float(skilldata[-1][0])
        print skill, total
        skillsgrade[0] += total
        skillsgrade[1] += 1

    skillsgrade[3] = skillsgrade[0]/ (4*skillsgrade[1])
    print skillsgrade[3]

    print "\n\nPARTICIPATION\n"
    print partgrade[3]

    print "\n\nLAB REPORTS\n"
    print labgrade[3]

    print "\n\nTOTAL    for ", NAME, "\n"
    total = partgrade[3]*partgrade[2] + labgrade[3]*labgrade[2] + skillsgrade[3]*skillsgrade[2]
    total += qgrade[3]*qgrade[2] + hwgrade[3]*hwgrade[2]
    print "Part.\tLab.\tSkills\tQuiz\tHW\tTotal"
    print("%.0f" % (partgrade[3]*100)),"\t",
    print "%.0f" % (100*labgrade[3]),"\t", 
    print "%.0f" % (100*skillsgrade[3]), "\t", 
    print "%.0f" % (100*qgrade[3]),"\t", 
    print "%.0f" % (100*hwgrade[3]),"\t",
    print "%.0f" % (100*total)
    print "-"*60
    print "\n\n\n\n"
    summary.write(NAME + ',' + str(partgrade[3]) + ',' + str(labgrade[3]) + ',' + str(skillsgrade[3]))
    summary.write(',' + str(qgrade[3]) + ',' + str(hwgrade[3]) + ',' + str(total) +'\n')

summary.close()

