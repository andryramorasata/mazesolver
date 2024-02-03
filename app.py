from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        root.title("My Maze Solver")
        canvas = Canvas(self.root, {"width":width, "height":height})
        canvas.pack()
        isRunning = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw():
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close():
        while self.isRunning:
            self.redraw()

    def close():
        self.isRunning = False

def main():
    win = Window(800, 600)
    win.wait_for_close()
