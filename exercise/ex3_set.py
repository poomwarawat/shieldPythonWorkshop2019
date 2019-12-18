#!/usr/bin/env python

##########################################################################
#   IMPORT
##########################################################################

import unittest
from typing import Set, List

##########################################################################
#   GLOBAL
##########################################################################

##########################################################################
#   HELPER
##########################################################################

def getFullFrameRange( frameSet : Set[int] ) -> Set[int]:
    ''' This function completes missing in-between frame numbers
        of given frame set
    '''

    #   Implement your code here
    raise NotImplementedError

def countSame( numList : List[int] ) -> int:
    ''' This function counts number of duplicated element within
        given list of numbers
    '''

    #   Implement your code here
    raise NotImplementedError

def getPrime( n : int ) -> Set[int]:
    ''' This function lists prime number from 2 (first prime number)
        to nth prime number
        NOTE - Assume that n is always >= 1
    '''

    #   Implement your code here
    raise NotImplementedError

##########################################################################
#   CLASS
##########################################################################

class Exercise3Test( unittest.TestCase ):

    def setUp(self):
        super(Exercise3Test, self).setUp()

    def test_getFullFrameRange(self):

        #   Case 1
        self.assertSetEqual(getFullFrameRange({1,5,10}),{1,2,3,4,5,6,7,8,9,10})

        #   Case 2
        self.assertRaises(ValueError, getFullFrameRange, {})

    def test_countSame(self):

        #   Case 1
        self.assertEqual(countSame([1,1,2,3,5]),1)

        #   Case 2
        self.assertEqual(countSame([1,1,1,1,1]),4)

        #   Case 3
        self.assertEqual(countSame([-2,-1,0,1,2]),0)

        #   Case 4
        self.assertEqual(countSame([]),0)

    def test_getPrime(self):

        #   Case 1
        self.assertSetEqual(getPrime(5),{2,3,5,7,11})

        #   Case 2
        self.assertSetEqual(getPrime(12),{2,3,5,7,11,13,17,19,23,29,31,37})

    def tearDown(self):
        super(Exercise3Test, self).tearDown()

##########################################################################
#   MAIN
##########################################################################

##########################################################################
#   RUN
##########################################################################

if __name__ == '__main__':
    unittest.main()