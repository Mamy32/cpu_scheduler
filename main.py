import tkinter as tk
from gui.interface import CPUSchedulerGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = CPUSchedulerGUI(root)
    root.mainloop()