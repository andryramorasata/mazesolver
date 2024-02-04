from tkinter import Tk, BOTH, Canvas

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

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self,canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y, 
            self.point2.x, self.point2.y,
            fill=fill_color,
            width=2
        )
        canvas.pack(fill="both", expand=True)

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(0,0), Point(800,600)), "red")
    win.wait_for_close()

main()
