import activity3
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test1(self):
        ''' given a list, swap element 1 for the next element'''
        inlist = [4,3,2,1]
        outlist = [4,2,3,1]
        assert (sorting.swap(inlist,1)==outlist) #test 1 fails, swap does not work as expected.

if __name__ == '__main__':
    unittest.main()
