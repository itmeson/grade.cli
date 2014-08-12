import readline

class MyCompleter(object):  # Custom completer
    """"Borrowed from http://stackoverflow.com/questions/7821661/how-to-code-autocompletion-in-python
    This class provides BASH style tab completion (1 tab gives match if there's a unique, 2 gives list of possible)
    """
    
    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:  # cache matches (entries that start with entered text)
		self.matches = [s for s in self.options 
                   if text in s]

                #self.matches = [s for s in self.options 
                #                    if s and s.startswith(text)]
            else:  # no text entered, all matches possible
                self.matches = self.options[:]

        # return match indexed by state
        try: 
            return self.matches[state]
        except IndexError:
            return None



import sys

#1. Go to the class directory, and get the list of names:
path = sys.argv[1]

# read in the names
namesF = path + "names.csv"#sys.argv[1]
namesFile = open(namesF, 'rU')
names = namesFile.readlines()
names = [n.strip() for n in names]
completer = MyCompleter(names)
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')


