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
    
    def wait_for_close(self):
        self.isRunning = True
        while self.isRunning:
            self.redraw()

    def close(self):
        self.isRunning = False

def main():
    win = Window(800, 600)
    win.wait_for_close()

main()
