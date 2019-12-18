#!/usr/bin/env python

##########################################################################
#   IMPORT
##########################################################################

import unittest
from typing import Dict, List, Optional
import math

##########################################################################
#   GLOBAL
##########################################################################

##########################################################################
#   HELPER
##########################################################################

def getUserName( userDataDict : Dict ) -> str:
    ''' This function simply gets user name from given user
        data dictionary
    '''

    #   Implement your code here
    raise NotImplementedError

def generateHalfLookUpDict( numList : List[float] ) -> Dict:
    ''' This function constructs a mapping dictionary from given
        list of numbers to their half value
    '''

    #   Implement your code here
    raise NotImplementedError

def getTreeHeight( tree : Dict, height : Optional[int]=0 ) -> int:
    ''' This function gets tree height by given dictionary which
        is structured like a tree and starting height (0 as default)
        NOTE - Assume that the given tree is always a valid tree structure
    '''

    #   Implement your code here
    raise NotImplementedError

##########################################################################
#   CLASS
##########################################################################

class Exercise4Test( unittest.TestCase ):

    def setUp(self):
        super(Exercise4Test, self).setUp()

    def test_getUserName(self):

        #   Case 1
        self.assertEqual(getUserName({ 'name' : 'Toddy', 'age' : 26, 'weight' : 50.4 }), 'Toddy')

        #   Case 2
        self.assertEqual(getUserName({ 'name' : 'Nhong', 'isGraduated' : False }), 'Nhong')

        #   Case 3
        self.assertRaises(AssertionError, getUserName, { 'age' : -1 })

    def test_generateHalfLookUpDict(self):
        
        #   Case 1
        self.assertDictEqual(generateHalfLookUpDict([0.5,1,1.5,2]), { 0.5: 0.25, 1:0.5, 1.5:0.75, 2:1 })

        #   Case 2
        self.assertDictEqual(generateHalfLookUpDict([-11.5,0,-11.5,-11.5]), { 0: 0, -11.5: -5.75 })

        #   Case 3
        self.assertDictEqual(generateHalfLookUpDict([]), dict())

    def test_getTreeHeight(self):

        #   Case 1
        self.assertEqual(getTreeHeight({'a':{'b':{'c':{}}}}), 3)

        #   Case 2
        self.assertEqual(getTreeHeight({'a':{'b':{'c':{}},'d':{'e':{},'f':{'g':{}}}}}), 4)

        #   Case 3
        self.assertEqual(getTreeHeight({}), 0)

    def tearDown(self):
        super(Exercise4Test, self).tearDown()

##########################################################################
#   MAIN
##########################################################################

##########################################################################
#   RUN
##########################################################################

if __name__ == '__main__':
    unittest.main()