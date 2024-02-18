from cell import Cell

class Maze:

    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__create_cells()

    def __create_cells(self):
        self.__cells = [[Cell(self.win) for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.__draw_cell(i,j)

    def __draw_cell(self, i, j):
        self.__cells[i][j].draw(
            self.x1 + (self.cell_size_x * i),
            self.y1 + (self.cell_size_y * j),
            (self.x1)+ (self.cell_size_x * (i+1)),
            (self.y1) + (self.cell_size_y * (j+1))
        )
        self.__animate()

    def __animate(self):
        self.win.root.after(50, self.win.redraw())
