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

def parsePAIRS(fname="grade.txt"):
    f = open(fname, 'rU')
    possibilities = {}
    for line in f:
	data = line.strip().split(';')
	for pair in data:
	    info = pair.strip().split(':')
	    key = info[0].strip().replace('\"','')
	    val = info[1].strip().replace('\"','')
	    if key not in possibilities:
		possibilities[key] = set([val])
	    else:
		possibilities[key].add(val)
    return possibilities


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
	    out = "date:" + todaysDATE + "; " 
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
	entry = {}
        for pair in data:
	    info = pair.strip().split(':')
	    
	    key = info[0].strip().replace('\"','')
	    val = info[1].strip().replace('\"','')
	    entry[key] = val
	if 'date' in entry.keys():
	    if entry['date'] == date:
	        present.append(entry['name'])
    present.sort()
    print "\n".join(present)


	     
	    
	


#names = readNames()

poss = parsePAIRS()
# Register our completer function
defaults =     {
     'stop':[],
     'attendance':[],
     'report Attendance':[]
    }
ActionDict = {'attendance':enterAttendance, 'report Attendance':reportAttendance}

completions = dict(defaults.items() + poss.items())

readline.set_completer(BufferAwareCompleter(completions).complete)

# Use the tab key for completion
readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')

# Prompt the user for text
input_loop(ActionDict)
