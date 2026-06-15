# main.py

import tkinter as tk
from gui.interface import CPUSchedulerGUI

root = tk.Tk()

app = CPUSchedulerGUI(root)

root.mainloop()