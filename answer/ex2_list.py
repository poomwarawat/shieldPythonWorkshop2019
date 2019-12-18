#!/usr/bin/env python

##########################################################################
#   IMPORT
##########################################################################

import unittest
from typing import List

##########################################################################
#   GLOBAL
##########################################################################

##########################################################################
#   HELPER
##########################################################################

def normalizePositive( s : List[float] ) -> List[float]:
    ''' This function normalizes elements with given list
        of positive floating point values with its maximum element
    '''

    assert( all([ x > 0 for x in s ]) )

    return [ x/max(s) for x in s ]

def quickSort( s : List[int] ) -> List[int]:
    ''' This function sorts given list with quick sort algorithm
    '''

    if len(s) == 0:
        return []

    return quickSort( [ x for x in s if x < s[0]] ) \
            + [ x for x in s if x == s[0] ] \
            + quickSort( [ x for x in s if x > s[0] ])

def decode( code : int ) -> str:
    ''' This function decodes given interger code as a string
        NOTE - Assume that given code is always non-negative integer
    '''

    answer = ''
    if code & 1 << 0:
        answer += 'a'
    if code & 1 << 1:
        answer += 'b'
    if code & 1 << 2:
        answer += 'c'

    return answer

##########################################################################
#   CLASS
##########################################################################

class Exercise2Test( unittest.TestCase ):

    def setUp(self):
        super(Exercise2Test, self).setUp()

    def test_noralize(self):

        #   Case 1
        self.assertListEqual( normalizePositive([3,1,2,4]), [0.75,0.25,0.5,1] )

        #   Case 2
        self.assertRaises( AssertionError, normalizePositive, [1,-2] )

    def test_quickSort(self):

        #   Case 1
        self.assertListEqual( quickSort([2,5,1,-1,1,9]), [-1,1,1,2,5,9] )

        #   Case 2
        self.assertListEqual( quickSort([]), [] )

        #   Case 3
        self.assertListEqual( quickSort([1,1,1]), [1,1,1] )

    def test_decode(self):

        #   Case 1
        self.assertEqual( decode(0), '' )
        self.assertEqual( decode(1), 'a' )
        self.assertEqual( decode(2), 'b' )
        self.assertEqual( decode(3), 'ab' )
        self.assertEqual( decode(4), 'c' )
        self.assertEqual( decode(5), 'ac' )
        self.assertEqual( decode(6), 'bc' )
        self.assertEqual( decode(7), 'abc' )

        #   Case 2
        self.assertEqual( decode(1024), '' )
        self.assertEqual( decode(9), 'a' )
        self.assertEqual( decode(42), 'b' )
        self.assertEqual( decode(91), 'ab' )
        self.assertEqual( decode(228), 'c' )
        self.assertEqual( decode(37), 'ac' )
        self.assertEqual( decode(22), 'bc' )
        self.assertEqual( decode(55), 'abc' )

    def tearDown(self):
        super(Exercise2Test, self).tearDown()

##########################################################################
#   MAIN
##########################################################################

##########################################################################
#   RUN
##########################################################################

if __name__ == '__main__':
    unittest.main()