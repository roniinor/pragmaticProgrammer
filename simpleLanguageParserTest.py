import unittest
import simpleLanguageParser

"""
Simple language parser test routines
"""

class TestLanguage(unittest.TestCase):
    
    def setUp(self):
        self.p = simpleLanguageParser.Parser()

    # validCommand to pick up commands in cmds dictionary only
    def test_validCommand(self):
        self.assertTrue(self.p.validCommand('P'))
        self.assertTrue(self.p.validCommand('E'))
        self.assertFalse(self.p.validCommand('PE'))
        self.assertFalse(self.p.validCommand('p'))
        self.assertFalse(self.p.validCommand(3))
        self.assertFalse(self.p.validCommand('p'))
        self.assertFalse(self.p.validCommand(''))
        
    # test command file turtleCommands_ex5.txt contains 7 commands
    # particular commands are matched below.
    def test_readcCommandFile(self):
        l = self.p.readCommandFile('turtleCommands_ex5.txt')
        self.assertEqual(len(l), 7)
        self.assertEqual(l[0], 'P 2 # select pen 2')
        self.assertEqual(l[6], 'U # pen up')
        
    # testing string output of parseCommand for now
    # final version of parseCommand to call function rather than 
    # output a string
    def test_parseCommandString(self):
        self.assertEqual(self.p.parseCommand('X 2 # select pen 2'),'INVALID COMMAND')
        self.assertEqual(self.p.parseCommand('P 2 # select pen 2'),'CALL: ' + self.p.cmds['P'][1] + ' ARG: 2' +' - COMMENT: select pen 2')
        self.assertEqual(self.p.parseCommand('U # pen up'),'CALL: ' + self.p.cmds['U'][1] + ' - COMMENT: pen up')
        self.assertEqual(self.p.parseCommand('N 3'),'CALL: ' + self.p.cmds['N'][1] + ' ARG: 3')
        self.assertEqual(self.p.parseCommand('D'),'CALL: ' + self.p.cmds['D'][1])
                
    def tearDown(self):
        pass
            
def main(args):
    unittest.main()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
    
