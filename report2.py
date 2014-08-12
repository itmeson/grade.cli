def hwGRADE(g, hw, NAME):
    """Compute average of hw scores and output HW feedback"""
    hwgrade = [0,0,0.1, 0]
    output = ""
    for h in hw:
        output += h['date'] + '\t' + h['hwid'] + '\n'
        for hwscore in g.GradeBook.names[NAME]['hwscore']:
            if hwscore['hwid'] == h['hwid']:
		output += " notes:" + hwscore['notes'] + " questions:" + hwscore['questions']
		output += " summaries:" + hwscore['summaries'] + '\n'
		if 'comment' in hwscore:
		    output += hwscore['comment'] + '\n'
		
                output +=  "\n"
                hwgrade[0] += float(hwscore['notes']) + float(hwscore['questions']) + float(hwscore['summaries'])

                hwgrade[1] += 1
    hwgrade[3] = hwgrade[0]/(12*hwgrade[1])
    return (output, hwgrade)


def qGRADE(g, quizzes, skillIDs, NAME):
    """Compute average of all quiz results and output quiz feedback"""
    qgrade = [0,0,0.2,0]
    quizRESULTS = {key: [] for key in skillIDs}
    output = ''
    for q in quizzes:
        output += q['date'] + '\t' + q['quizname'] + '\n'
	if 'quizscore' not in g.GradeBook.names[NAME]:
	    print NAME
	    return ('No quizzes taken', qgrade)
        for quizscore in g.GradeBook.names[NAME]['quizscore']:
            if quizscore['quizname'] == q['quizname']:
                output += "  " + quizscore['skill'] + ' '
                output += "  " +  quizscore['score'] +  "/4\n" +  quizscore.get('comment', '')
                output += "\n\n"
                qgrade[0] += float(quizscore['score'])
                qgrade[1] += 1
                quizRESULTS[quizscore['skill']].append((quizscore['score'], quizscore['date']))
    qgrade[3] = qgrade[0] / (4*qgrade[1])
    return (output, qgrade)


def skillGRADE(g, skillIDs, NAME):
    """Compute average score for each skill and output skill results.  Currently uses 60% rule."""
    sgrade = [0,0,0.3,0]
    skillRESULTS = {key: [] for key in skillIDs}
    output = ''
    if 'quizscore' not in g.GradeBook.names[NAME]:
	return ('No Skills Taken', sgrade)
    for score in g.GradeBook.names[NAME]['quizscore']:
	skill = score['skill']
	result = float(score['score'])
	skillRESULTS[skill].append(result)
    skillDEFS = {x['skill']:x['description'] for x in g.GradeBook.things['standard']}
    for skill in skillIDs:
	output += skill + '\t' + skillDEFS[skill] + '\n\t'
	scores = skillRESULTS[skill]
	if len(scores) == 0:
	    output += 'No data for this skill'
	elif len(scores) == 1:
	    output += str(scores[0])
	    sgrade[0] += scores[0]
	    sgrade[1] += 1
	else:
	    nscores = len(scores) - 1
	    average = 0.4*sum(scores[:-1])/nscores + 0.6*scores[-1]
	    output += str(average)
	    sgrade[0] += average
	    sgrade[1] += 1
	output += '\n\n'
    sgrade[3] = sgrade[0]/(4*sgrade[1])
    return (output, sgrade)


def partGRADE(g, parts, NAME):
    """Compute participation score"""
    pgrade = [0,0,0.1,0]
    output = ""
    for p in parts:
        output += p['date'] + '\t' + p['partid'] + '\n'
        for partscore in g.GradeBook.names[NAME]['partscore']:
            if partscore['partid'] == p['partid']:
		output += "\t" + str(round(float(partscore['score']), 1)) + "  out of 100\n" 
                output +=  "\n"
                pgrade[0] += float(partscore['score']) 
                pgrade[1] += 1
    pgrade[3] = pgrade[0]/(100*pgrade[1])
    return (output, pgrade)


def labGRADE(g, labs, NAME):
    """Compute participation score"""
    lgrade = [0,0,0.3,0]
    output = ""
    for l in labs:
        output += l['date'] + '\t' + l['labid'] + '\n'
        for labscore in g.GradeBook.names[NAME]['labscore']:
            if labscore['labid'] == l['labid']:
		output += "\t" + str(round(float(labscore['score']), 1)) + "  out of 100\n" 
                output +=  "\n"
                lgrade[0] += float(labscore['score']) 
                lgrade[1] += 1
    lgrade[3] = lgrade[0]/(100*lgrade[1])
    return (output, lgrade)



def overallGRADE(things):
    overall = 0
    for t in things:
	overall += t[1][3]*t[1][2]
	overall = round(overall, 2)
    if overall >= 0.93:
	letter = 'A'
    elif overall < 0.93 and overall >= 0.9:
	letter = 'A-'
    elif overall < 0.9 and overall >= 0.87:
	letter = 'B+'
    elif overall < 0.87 and overall >= 0.83:
	letter = 'B'
    elif overall < 0.83 and overall >= 0.80:
	letter = 'B-'
    elif overall < 0.80 and overall >= 0.77:
	letter = 'C+'
    elif overall < 0.77 and overall >= 0.73:
	letter = 'C'
    elif overall < 0.73 and overall >= 0.7:
	letter = 'C-'
    elif overall < 0.7 and overall >= 0.67:
	letter = 'D+'
    elif overall < 0.67 and overall >= 0.55:
	letter = 'Pass'
    elif overall <= 0.5:
	letter = 'Incomplete'
    return (overall, letter)
   
