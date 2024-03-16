from cell import Cell
import random

class Maze:

    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = seed
        self.__create_cells()
        #random.seed(seed)
        if num_cols > 0 and num_rows > 0:
            self._break_walls_r(random.randrange(0,num_cols-1),random.randrange(0,num_rows-1))
        self._reset_cells_visited()
        
    def __create_cells(self):
        self._cells =[]
        for i in range(self.num_cols):
            self._cells.append([])
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self.win))
                
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.__draw_cell(i,j)
        if self.num_cols > 0 and self.num_rows > 0:
            self._break_entrance_and_exit()


    def __draw_cell(self, i, j):
        if self.win is None:
            return
        self._cells[i][j].draw(
            self.x1 + (self.cell_size_x * i),
            self.y1 + (self.cell_size_y * j),
            (self.x1)+ (self.cell_size_x * (i+1)),
            (self.y1) + (self.cell_size_y * (j+1))
        )
        self.__animate()

    def __animate(self):
        self.win.root.after(50, self.win.redraw())

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self.__draw_cell(0,0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self.__draw_cell(self.num_cols-1, self.num_rows-1)

    def _get_adjacent_cells(self,i,j):
        
        adjacent_cells = []
        if i - 1 >= 0 and not self._cells[i-1][j].visited:
            adjacent_cells.append((i-1,j))
        if i + 1 < self.num_cols and not self._cells[i+1][j].visited:
            adjacent_cells.append((i+1,j))
        if j - 1 >= 0 and not self._cells[i][j-1].visited:
            adjacent_cells.append((i, j-1))
        if j + 1 < self.num_rows and not self._cells[i][j+1].visited:
            adjacent_cells.append((i, j+1))
        return adjacent_cells

    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True
        while True:
            cells_to_visit = []
            for adjacent_cell in self._get_adjacent_cells(i,j):
                if not self._cells[adjacent_cell[0]][adjacent_cell[1]].visited:
                    cells_to_visit.append(adjacent_cell)
            if len(cells_to_visit) == 0:
                self.__draw_cell(i,j)
                return

            random.seed(self.seed)
            next_direction = random.randrange(0,len(cells_to_visit),1)
            next_cell = cells_to_visit[next_direction]
            is_same_col = (i == next_cell[0])
            is_same_row = (j == next_cell[1])
            is_next_cell_down = (j < next_cell[1])
            is_next_cell_right = (i < next_cell[0])

            if is_same_row and is_next_cell_right:
                self._cells[i][j].has_right_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_left_wall = False
            elif is_same_row and not is_next_cell_right:
                self._cells[i][j].has_left_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_right_wall = False
            elif is_same_col and is_next_cell_down:
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_top_wall = False
            elif is_same_col and not is_next_cell_down:
                self._cells[i][j].has_top_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_botoom_wall = False

            if self.win is not None:
                self.win.redraw()
            self._break_walls_r(next_cell[0],next_cell[1])

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False

    def _solve_r(self,i,j):
        self.__animate()
        self._cells[i][j].visited = True
        
        if i == (self.num_cols - 1) and j == (self.num_rows - 1):
            return True
        for adjacent_cell in self._get_adjacent_cells(i,j):
            is_same_col = (i == adjacent_cell[0]) 
            is_same_row = (j == adjacent_cell[1])
            is_next_cell_down = (j < adjacent_cell[1])
            is_next_cell_right = (i < adjacent_cell[0])
            if (
                    is_same_row and 
                    is_next_cell_right and not
                    self._cells[adjacent_cell[0]][adjacent_cell[1]].has_left_wall
                ):
                self._cells[i][j].draw_move(self._cells[adjacent_cell[0]][adjacent_cell[1]])
                if self._solve_r(adjacent_cell[0], adjacent_cell[1]):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[adjacent_cell[0]][adjacent_cell[1]],True)

            elif (
                    is_same_row and not 
                    is_next_cell_right and not
                    self._cells[adjacent_cell[0]][adjacent_cell[1]].has_right_wall
                ):
                self._cells[i][j].draw_move(self._cells[adjacent_cell[0]][adjacent_cell[1]])
                if self._solve_r(adjacent_cell[0], adjacent_cell[1]):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[adjacent_cell[0]][adjacent_cell[1]],True)
 
            elif (
                    is_same_col and 
                    is_next_cell_down and not
                    self._cells[adjacent_cell[0]][adjacent_cell[1]].has_top_wall
                    
                ):
                self._cells[i][j].draw_move(self._cells[adjacent_cell[0]][adjacent_cell[1]])
                if self._solve_r(adjacent_cell[0], adjacent_cell[1]):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[adjacent_cell[0]][adjacent_cell[1]],True)

            elif(
                    is_same_col and not
                    is_next_cell_down and not
                    self._cells[adjacent_cell[0]][adjacent_cell[1]].has_bottom_wall
                ):
                self._cells[i][j].draw_move(self._cells[adjacent_cell[0]][adjacent_cell[1]])
                if self._solve_r(adjacent_cell[0], adjacent_cell[1]):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[adjacent_cell[0]][adjacent_cell[1]],True)

        return False

    def solve(self):
        return  self._solve_r(0,0)
