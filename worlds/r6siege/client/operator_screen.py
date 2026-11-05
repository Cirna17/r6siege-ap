import tkinter as tk
import tkinter.ttk as ttk
from ctypes import windll
from .. import operator_data

operators = tk.Tk(screenName = None, baseName = None, className = 'Tk', useTk = 1)

#Scale to real screen resolution to make text less blurry
try:
    windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass

operators.title("Rainbow Six Siege Archipelago")