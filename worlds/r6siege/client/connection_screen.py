import tkinter as tk
import tkinter.ttk as ttk
from ctypes import windll

root = tk.Tk(screenName = None, baseName = None, className = 'Tk', useTk = 1)

#Scale to real screen resolution to make text less blurry
try:
    windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass

root.title("Connection info")

entry_frame = tk.Frame(root)
connection_button_frame = tk.Frame(root)

tk.Label(entry_frame, text = "Host: ").grid(row = 0, column = 0)
tk.Label(entry_frame, text = "Port: ").grid(row = 1, column = 0)
tk.Label(entry_frame, text = "Slot: ").grid(row = 2, column = 0)

host = tk.StringVar()
port = tk.StringVar()
slot = tk.StringVar()

host.set("archipelago.gg")

def connect() -> None:
    print(host.get(), port.get(), slot.get())

host_entry = tk.Entry(entry_frame, textvariable = host).grid(row = 0, column = 1)
port_entry = tk.Entry(entry_frame, textvariable = port).grid(row = 1, column = 1)
slot_entry = tk.Entry(entry_frame, textvariable = slot).grid(row = 2, column = 1)

connect_button = tk.Button(connection_button_frame, text = "Connect", width = 25, justify = tk.CENTER, command = connect)
connect_button.pack()

entry_frame.pack()
connection_button_frame.pack()

error_label = tk.Label(text = "Error: unable to connect.", fg = "red")
error_label.pack()

root.mainloop()