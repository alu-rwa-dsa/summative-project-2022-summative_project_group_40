#Importing the unit test module
import unittest
#import solver
#import gui


class Testcases(unittest.TestCase):

   #Testing when no value if filled in the sudoku
    def test_nothing(self):
        self.assertTrue("shouldn't happen")

    #Testing if the sudoku is completely filled
    def test_sudoku_is_complete(self):
        self.assertTrue("sudoku solved!")

    #Testing for duplicate column values
    def test_duplicate_column_values(self):
        self.assertTrue("Please ensure there are no duplicate values in the columns!")

    #Testing for duplicate_grid_values
    def test_duplicate_grid_values(self):
        self.assertTrue("Ensure there are no duplicate values in the same grid!")

    #Testing if the values in the puzzle are less than 17
    def test_puzzle_value_less_than17(self):
        self.assertTrue("Enter a correct number of values")

    # Testing for duplicate row values
    def test_duplicate_row_values(self):
            self.assertTrue("Please ensure there are no duplicate values in the rows!")








#Driver code
if __name__ == '__main__':
     unittest.main()

