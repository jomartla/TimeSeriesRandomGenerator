from tkinter import ttk, messagebox
import tkinter as tk

from Frames.MainFrame import MainFrame


class Application(ttk.Frame):
    def __init__(self, main_w):
        super().__init__(main_w)

        main_w.title("Data mining")

        # Create tab panel
        self.notebook = ttk.Notebook(self)

        self.mainframe = MainFrame(self.notebook)
        self.notebook.add(
            self.mainframe, text="Main")

        self.notebook.pack()
        self.pack()


# Setting window size.
main_window = tk.Tk()
app = Application(main_window)
'''
Mainloop is an endless loop of the window
The window will wait for any user interaction till we close it
'''
app.mainloop()
