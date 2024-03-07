import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_no_rows(self):
        num_cols = 5
        num_rows = 0
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m2._cells),
            num_cols,
        )
        self.assertEqual(
            len(m2._cells[0]),
            num_rows
        )

    def test_maze_no_cols(self):
        num_cols = 0
        num_rows = 5
        m3 = Maze(0,0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m3._cells),
            num_cols,
        )
        with self.assertRaises(IndexError):
            len(m3._cells[0])
        
    def test_maze_entrance_and_exit(self):
        num_cols = 5
        num_rows = 10
        m4 = Maze(0,0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m4._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m4._cells[num_cols-1][num_rows-1].has_bottom_wall,
            False
        )

    def test_reset_visit(self):
        num_cols = 3
        num_rows = 3
        m4 = Maze(0,0, num_rows, num_cols, 10, 10)
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertEqual(
                    m4._cells[i][j].visited,
                   False
                )
if __name__ == "__main__":
    unittest.main()
