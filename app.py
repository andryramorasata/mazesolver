from tkinter import Tk, BOTH, Canvas
from geometry import Point, Line
from cell import Cell
from maze import Maze

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
    maze = Maze(20, 20, 8, 8, 78, 58, win, 7)
    win.wait_for_close()
if __name__ == "__main__":
    main()
