import tkinter as tk

from josephus.adapter.tk_interface import TkWindow

if __name__ == '__main__':
    root = tk.Tk()
    my_window = TkWindow(root)
    root.mainloop()