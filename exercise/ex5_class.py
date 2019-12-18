#!/usr/bin/env python

##########################################################################
#   IMPORT
##########################################################################

import unittest
from typing import Optional

##########################################################################
#   GLOBAL
##########################################################################

##########################################################################
#   HELPER
##########################################################################

##########################################################################
#   CLASS
##########################################################################

class Vector3(object):

    def __init__(self, x : Optional[float]=0, y : Optional[float]=0, z : Optional[float]=0) -> 'Vector3':

        self.x = x
        self.y = y
        self.z = z
    
    def dot( self, v : 'Vector3') -> float:
        return self.x*v.x + self.y*v.y + self.z*v.z

    def cross( self, v : 'Vector3') -> 'Vector3':
        return Vector3( self.y*v.z - self.z*v.y,\
                        self.z*v.x - self.x*v.z,\
                        self.x*v.y - self.y*v.x  )

    def __add__(self, v : 'Vector3') -> 'Vector3':
        
        #   Implement your code here
        raise NotImplementedError

    def __neg__(self) -> 'Vector3':

        #   Implement your code here
        raise NotImplementedError

    def __sub__(self, v : 'Vector3') -> 'Vector3':
        
        #   Implement your code here
        raise NotImplementedError

    def __mul__(self, k : float) -> 'Vector3':
        
        #   Implement your code here
        raise NotImplementedError

    def __rmul__(self, k : float) -> 'Vector3':
        
        #   Implement your code here
        raise NotImplementedError

    def __eq__(self, v : 'Vector3') -> bool:
        return all( [ self.x == v.x, self.y == v.y, self.z == v.z ] )

    def __str__(self) -> str:
        return 'Vector3({},{},{})'.format(self.x, self.y, self.z)

class Exercise5Test( unittest.TestCase ):

    def setUp(self):
        super(Exercise5Test, self).setUp()

    def test_add(self):

        #   Case 1
        self.assertEqual(Vector3(1,2,3)+Vector3(4,5,6), Vector3(5,7,9))

    def test_sub(self):

        #   Case 1
        self.assertEqual(Vector3(1,2,3)-Vector3(4,5,6), Vector3(-3,-3,-3))

        #   Case 2
        self.assertEqual(-Vector3(4,5,6)+Vector3(1,2,3), Vector3(-3,-3,-3))

    def test_mul(self):

        #   Case 1
        self.assertEqual(5*Vector3(1,2,3), Vector3(5,10,15))

        #   Case 2
        self.assertEqual(Vector3(1,2,3)*-5, Vector3(-5,-10,-15))

    def tearDown(self):
        super(Exercise5Test, self).tearDown()

##########################################################################
#   MAIN
##########################################################################

##########################################################################
#   RUN
##########################################################################

if __name__ == '__main__':
    unittest.main()