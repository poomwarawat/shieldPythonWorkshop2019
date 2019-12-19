#!/usr/bin/env python

##########################################################################
#   IMPORT
##########################################################################

import unittest

##########################################################################
#   GLOBAL
##########################################################################

##########################################################################
#   HELPER
##########################################################################

def divide( a : float, b : float ) -> float:
    ''' This function divides two given floating points numbers
    '''

    return a/b
    
class Exercise1Test( unittest.TestCase ):

    def setUp(self):
        super(Exercise1Test, self).setUp()

    def test_divide(self):

        #   Case 1
        self.assertEqual( divide(3,3), 1 )

        #   Case 2
        self.assertEqual( divide(-1,2), -0.5 )

        #   Case 3
        self.assertRaises( ZeroDivisionError, divide, 0, 0 )

    def tearDown(self):
        super(Exercise1Test, self).tearDown()

##########################################################################
#   MAIN
##########################################################################

##########################################################################
#   RUN
##########################################################################

if __name__ == '__main__':
    unittest.main()