import readline
import logging
import time

#Code borrowed from http://pymotw.com/2/readline/
# The readline tutorial in Python Module of the Week


LOG_FILENAME = '/tmp/completer.log'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    )

class BufferAwareCompleter(object):
    
    def __init__(self, options):
        self.options = options
        self.current_candidates = []
        return

    def complete1(self, text, state):
	response = None
	if state == 0:
	    origline = readline.get_line_buffer()
	    begin = readline.get_begidx()
	    end = readline.get_endidx()
	    being_completed = origline[begin:end]
	    words = origline.split()

	    if not words:
		self.curent_candidates = sorted(self.options)
	    else:
	        try:
		    candidates = self.options
		    if being_completed:
			self.current_candidates = [ w for w in candidates
						   if being_completed in w]
		    else:
			self.current_candidates = candidates


                except (KeyError, IndexError), err:
                    self.current_candidates = []
        try:
            response = self.current_candidates[state]
        except IndexError:
            response = None
        return response

    def comp(self, text, state):
	response = None
	if state == 0:
            # This is the first time for this text, so build a match list.
            origline = readline.get_line_buffer()
            begin = readline.get_begidx()
            end = readline.get_endidx()
            being_completed = origline[begin:end]
            words = origline.split(';')
	    
            logging.debug('origline=%s', repr(origline))
            logging.debug('begin=%s', begin)
            logging.debug('end=%s', end)
            logging.debug('being_completed=%s', being_completed)
            logging.debug('words=%s', words)
            
            if not words:
                self.current_candidates = sorted(self.options.keys())
            else:
                try:
                    if begin == 0:
                        # first word
                        candidates = self.options.keys()
                    else:
                        # later word
                        first = words[0]
                        candidates = self.options[first]
                    
                    if being_completed:
                        # match options with portion of input
                        # being completed
                        self.current_candidates = [ w for w in candidates
                                                    #if w.startswith(being_completed) ]
						   if being_completed in w ]
                    else:
                        # matching empty string so use all candidates
                        self.current_candidates = candidates

                    logging.debug('candidates=%s', self.current_candidates)
                    
                except (KeyError, IndexError), err:
                    logging.error('completion error: %s', err)
                    self.current_candidates = []
        
        try:
            response = self.current_candidates[state]
        except IndexError:
            response = None
        logging.debug('complete(%s, %s) => %s', repr(text), state, response)
        return response
            




    def complete(self, text, state):
        response = None
        if state == 0:
            # This is the first time for this text, so build a match list.
            
            origline = readline.get_line_buffer()
            begin = readline.get_begidx()
            end = readline.get_endidx()
            being_completed = origline[begin:end]
            words = origline.split()

            logging.debug('origline=%s', repr(origline))
            logging.debug('begin=%s', begin)
            logging.debug('end=%s', end)
            logging.debug('being_completed=%s', being_completed)
            logging.debug('words=%s', words)
            
            if not words:
                self.current_candidates = sorted(self.options.keys())
            else:
                try:
                    if begin == 0:
                        # first word
                        candidates = self.options.keys()
                    else:
                        # later word
                        first = words[0]
                        candidates = self.options[first]
                    
                    if being_completed:
                        # match options with portion of input
                        # being completed
                        self.current_candidates = [ w for w in candidates
                                                    #if w.startswith(being_completed) ]
						   if being_completed in w ]
                    else:
                        # matching empty string so use all candidates
                        self.current_candidates = candidates

                    logging.debug('candidates=%s', self.current_candidates)
                    
                except (KeyError, IndexError), err:
                    logging.error('completion error: %s', err)
                    self.current_candidates = []
        
        try:
            response = self.current_candidates[state]
        except IndexError:
            response = None
        logging.debug('complete(%s, %s) => %s', repr(text), state, response)
        return response
            

def input_loop(ActionDict):
    line = ''
    while line != 'stop':
        line = raw_input('Prompt ("stop" to quit): ')
	if line in ActionDict:
	    ActionDict[line]()
        print 'Dispatch %s' % line

def readNames(fname="grade.txt"):
    f = open(fname, 'rU')
    names = []
    for line in f:
	data = line.strip().split(";")
	if data[0].split(":")[0] == "name":
	    x = data[0].split(":")[1].replace("\"", "")
	    names.append(x)
    return names


class Grade():
    def __init__(self, fname="grade.txt"):
	self.fname = fname	
	self.parsePAIRS()

    def parsePAIRS(self):
	f = open(self.fname, 'rU')
        self.possibilities = {}
	self.dataTYPES = set(['stop'])
        for line in f:
	    data = line.strip().split(';')
	    for pair in data:
	        info = pair.strip().split(':')
	        if len(info) == 1:   #this means it's content type
		    self.dataTYPES.add(info[0])
	        else:
	    	    key = info[0].strip().replace('\"','')
	    	    val = info[1].strip().replace('\"','')
	    	    if key not in self.possibilities:
			self.possibilities[key] = set([val])
	    	    else:
			self.possibilities[key].add(val)
   

    def parseDATA(self):
	f = open(self.fname,'rU')
	self.names = {x:{} for x in self.possibilities['name']}
	self.things = {}#x:[] for x in self.dataTYPES}
	for line in f:
	    data = line.strip().split(';')
	    dataTYPE = data[0]
	    results = {}	    
            for pair in data[1:]:
	        info = pair.strip().split(':')
	        if len(info) == 1:
		    print line 
		key = info[0].strip().replace('\"','')
		val = info[1].strip().replace('\"','')
		results[key] = val
	    if 'name' in results:
		student = results.pop('name', None)
		if dataTYPE in self.names[student]:
		    self.names[student][dataTYPE].append(results)
	  	else:
		    self.names[student][dataTYPE] = [results]		
	    else:
		##this means it's a thing definition
		if dataTYPE in self.things:
            	    self.things[dataTYPE].append(results)
		else:
		    self.things[dataTYPE] = [results]
 

    def outputLine(self, entryType, lineData):
	f = open(self.fname, 'a')
	line = entryType + '; '
	for key in lineData.keys()[:-1]:
	    line +=  key + ':' + lineData[key] + '; '
	line += lineData.keys()[-1] + ':' + lineData[lineData.keys()[-1]]
	f.write(line+ '\n')
	f.close()



    def input_loop2(self, completions):
        line = ''
        entryType = ''
	lineData = {}
	while line != 'stop':
	    print "Current buffer:\t", lineData
	    lineData.pop('comment',0)     ## Do not reuse the comment field from one line to the next.
					   ## There is probably a better way to do this
	    readline.set_completer(BufferAwareCompleter(self.dataTYPES).complete1)
            temp = raw_input('Entry type ("stop") to quit)[enter] to use default\n')
            if temp == 'stop':
	        break

	    if temp != '' and temp != entryType:
		lineData = {}
		entryType = temp
	    
	    if entryType == "standard" or entryType == "quiz" or entryType == "hw":
	        key = "date"
            else:
		key = 'name'

            while key != '':
    	        if key == 'name':
		    readline.set_completer(BufferAwareCompleter(completions[key]).complete1)
		    val = raw_input('NAME:\t')
		    if val == '':
	                readline.set_completer(BufferAwareCompleter(completions).complete)
			break
		    lineData[key] = val
		    key = 'temp'
		    continue

		key = ''
	        readline.set_completer(BufferAwareCompleter(completions).complete)
	
                key = raw_input('Key, [enter] to continue to next line ')
                if key == '':
	            self.outputLine(entryType, lineData)
	            break
		elif key == 'stop':
		    break
	        if key in completions:
	            readline.set_completer(BufferAwareCompleter(completions[key]).complete1)
	
	        val = raw_input('Val:\t')
		if val == 'stop':
		    break
		lineData[key] = val




def enterAttendance():
    comp = completions['name']
    readline.set_completer(BufferAwareCompleter(comp).complete1)

    output = open('grade.txt', 'a')
    line = ''
    todaysDATE = time.strftime('%m/%d/%Y')
    while line != 'stop':
        line = raw_input('Enter names of those that are present. Enter ("stop" to quit): ')
	if line == 'stop':
	    break
        else:
	    out = "att; date:" + todaysDATE + "; " 
	    name = line.strip().replace('name ','') 
	    out += "name:" + name + "; "
	    out += "present:1\n"
	    output.write(out) 
    output.close()
    readline.set_completer(BufferAwareCompleter(completions).complete)

    
def reportAttendance(date=time.strftime('%m/%d/%Y')):
    date = raw_input('What date?')
    f = open('grade.txt', 'rU')
    present = []
    for line in f:
        data = line.strip().split(';')
	if data[0] != "att":
	    continue
	entry = {}
        for pair in data[1:]:
	    info = pair.strip().split(':')
	    
	    key = info[0].strip().replace('\"','')
	    val = info[1].strip().replace('\"','')
	    entry[key] = val
	if 'date' in entry.keys():
	    if entry['date'] == date:
	        present.append(entry['name'])
    present.sort()
    print "\n".join(present)



	     
	    
import sys

fname = "grade.txt"   #change this option to point to a different grade file.
			#TODO: change this to go into a config file
	
GradeBook = Grade(fname)

if __name__ == "__main__":
    print GradeBook.dataTYPES
    defaults =     {
         'stop':[],
         'att':[],
         }
    ActionDict = {'att':enterAttendance, 'report Attendance':reportAttendance}

    completions = dict(defaults.items() + GradeBook.possibilities.items())#poss.items())

    readline.set_completer(BufferAwareCompleter(completions).complete)

# Use the tab key for completion
    readline.parse_and_bind('tab: complete')
    readline.parse_and_bind('set editing-mode vi')

# Prompt the user for text
#input_loop(ActionDict)
    GradeBook.input_loop2(completions)
