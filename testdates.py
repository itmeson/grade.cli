import datetime

f = open('grade.txt', 'rU')
n = 0
dates = []
for line in f:
    data = line.strip().split(';')
    for d in data:
	pair = d.strip().split(':')
	if len(pair) == 2:
	    if pair[0] == 'date':
		date = datetime.datetime.strptime(pair[1], '%m%d%Y')
		dates.append((n, pair[1]))
    n += 1

dates.sort(key=lambda x: datetime.datetime.strptime(x[1], '%m%d%Y'))
print dates
