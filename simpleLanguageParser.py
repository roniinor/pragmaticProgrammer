#  March 2018 - simple language parsing
#  exercise from book The Pragmatic Programmer, A Hunt, D Thomas. Addison Wesley
#  Ch 2 A pragmatic approach, Ex 5 Domain languages
#  pdf version in documents/pythonVarious/

#  MAIN OBJ here is the pragmatic programmer and developing skills for this
#  -> using test driven development. Creating tests in the test routine 
#     BEFORE creating the modules in this class below.
#     Refresing python on the way 

"""
Simple language parser
"""
class Parser():
    
    # constants - command requires argument or not
    NO_ARG = 0
    ARG = 1
    
    # command dictionary
    cmds = {'P': [ARG, 'doSelectPen'],
        'U': [NO_ARG, 'doPenUp'],
        'D': [NO_ARG, 'doPenDown'],
        'N': [ARG, 'doPenDir'],
        'E': [ARG, 'doPenDir'],
        'S': [ARG, 'doPenDir'],
        'W': [ARG, 'doPenDir']}
    
    #c is a single letter command found in cmds dictionary
    def validCommand(self, c):
        return c in self.cmds.keys()

    #reads text file fname into list by line and returns list 
    def readCommandFile(self, fname):
        with open(fname) as f:
            read_data = f.readlines()
        read_data = [x.rstrip('\n') for x in read_data]
        return read_data
    
    #break down a command line, return a string representation
    #final version would actually call the routine for the command.
    def parseCommand(self, l):
        listl = l.split(' ')
        cs = ''
        c = listl[0]
        if not self.validCommand(c):
            return 'INVALID COMMAND'
        else:
            # command from cmds dict
            cs = 'CALL: ' + self.cmds[c][1]
            # if cmd needs argument then get that
            if self.cmds[c][0] == self.ARG:
                cs += ' ARG: ' + listl[1]
                # get comment
                try:
                    gotComment = listl[2]
                except IndexError:
                    gotComment = 'null'
                if gotComment == '#':
                    cs += ' - COMMENT:'
                    for cw in listl[3:]:
                        cs += ' ' + cw
            else:
                # No argument - get comment
                try:
                    gotComment = listl[1]
                except IndexError:
                    gotComment = 'null'
                if gotComment == '#':
                    cs += ' - COMMENT:'
                    for cw in listl[2:]:
                        cs += ' ' + cw
        return cs
        
def main(args):
    p = Parser()
    print(p.cmds['P'])
    cl = p.readCommandFile('turtleCommands_ex5.txt')
    for c in cl:
        print(c + ' -> ' + p.parseCommand(c))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
