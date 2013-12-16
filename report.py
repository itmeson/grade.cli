import grade as g


poss = g.GradeBook.possibilities

for p in poss:
    print p
    for item in poss[p]:
	print item,
    print "\n\n"


g.GradeBook.parseDATA()

for name in g.GradeBook.names:
    print name
    for item in g.GradeBook.names[name]:
        print "\t", item
	for res in g.GradeBook.names[name][item]:
	    print "\t\t", res
	print "\n"
    print "\n\n"


for t in g.GradeBook.things:
    print t, '\n\t', g.GradeBook.things[t]
