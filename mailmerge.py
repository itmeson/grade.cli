names = open('firstnames.txt', 'rU')
templateF = open('temp.txt', 'rU')
template = templateF.readlines()
templateF.close()
output = open('comments.txt', 'w')

for n in names:
    output.write('Dear ' + n.strip() + ',\n\n')
    output.write('\n'.join(template))

names.close()
output.close()
