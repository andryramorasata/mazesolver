from tkinter import Tk, BOTH, Canvas
from geometry import Point, Line
from cell import Cell

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("My Maze Solver")
        self.canvas = Canvas(self.root, {"width":width, "height":height})
        self.canvas.pack(fill="both", expand = True)
        self.isRunning = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def draw_line(self,line, fill_color):
        line.draw(self.canvas, fill_color)

    def wait_for_close(self):
        self.isRunning = True
        while self.isRunning:
            self.redraw()

    def close(self):
        self.isRunning = False

def main():
    win = Window(800, 600)
    cell = Cell(win, 50,50,100,100)
    cell_2 = Cell(win,150,150,200,200)
    cell.draw()
    cell_2.draw()
    cell.draw_move(cell_2)
    win.wait_for_close()

main()
