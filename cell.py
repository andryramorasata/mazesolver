from geometry import Point, Line

class Cell:
    def __init__(
        self,
        win,
        has_left_wall=True,
        has_right_wall=True,
        has_top_wall=True,
        has_bottom_wall=True
        ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.__win = win

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        
        if self.has_left_wall:
            left_wall = Line(
                Point(self.__x1, self.__y1),
                Point(self.__x1, self.__y2)
            )
            self.__win.draw_line(left_wall,"black")
            
        if self.has_right_wall:
            right_wall = Line(
                Point(self.__x2, self.__y1),
                Point(self.__x2, self.__y2)
            )
            self.__win.draw_line(right_wall, "black")

        if self.has_top_wall:
            top_wall = Line(
                Point(self.__x1, self.__y1),
                Point(self.__x2, self.__y1)
            )
            self.__win.draw_line(top_wall,"black")

        if self.has_bottom_wall:
            bottom_wall = Line(
                Point(self.__x1, self.__y2),
                Point(self.__x2, self.__y2)
            )
            self.__win.draw_line(bottom_wall,"black")

    def get_center_point(self):
        mid_x = (self.__x1 + self.__x2)/2
        mid_y = (self.__y1 + self.__y2)/2
        return Point(mid_x, mid_y)

    def draw_move(self, to_cell, undo=False):
        line_color = "red"
        if undo:
            line_color = "gray"
        move = Line(self.get_center_point(), to_cell.get_center_point())
        self.__win.draw_line(move, line_color)


