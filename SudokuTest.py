import unittest
from sudoku_Solver import read_game,solve_game

class TestSudokuGame(unittest.TestCase):
    def testSimple(self):
        game = read_game("Sudoku.txt")
        answer = read_game("SolSudoku.txt")
        solve_game(game)
        self.assertEqual(game,answer)
    def testHard(self):
        game = read_game("Hard.txt")
        answer = read_game("SolHard.txt")
        solve_game(game)
        self.assertEqual(game,answer)
    def testExtreme(self):
        game = read_game("Extreme.txt")
        answer = read_game("SolExtreme.txt")
        solve_game(game)
        self.assertEqual(game,answer)

if __name__ == '__main__':
    unittest.main()
        

