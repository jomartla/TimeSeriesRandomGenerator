from Frames.CSVFrame import CSVFrame
from Frames.SettingsFrame import SettingsFrame
from Frames.Settings.Parameters import Parameters
from Frames.ConfigurationFilesFrame import ConfigurationFilesFrame
from tkinter import ttk, messagebox
import tkinter as tk


class Application(ttk.Frame):
    def __init__(self, main_w):
        super().__init__(main_w)
        main_w.title("Time series random generator")

        main_w.protocol("WM_DELETE_WINDOW", self.close_window)

        # Read variables from conf file
        Parameters.read_parameters_from_conf_file()

        # Create tab panel
        self.notebook = ttk.Notebook(self)

        self.settingsframe = SettingsFrame(self.notebook)
        self.notebook.add(
            self.settingsframe, text="Settings")

        self.csv_frame = CSVFrame(self.notebook)
        self.notebook.add(
            self.csv_frame, text="CSV", padding=10)
        Parameters.csv_frame = self.csv_frame

        self.configuration_files_frame = ConfigurationFilesFrame(self.notebook)
        self.notebook.add(
            self.configuration_files_frame, text="Conf files", padding=10)

        self.notebook.pack()
        self.pack()

    @staticmethod
    def close_window():
        answer = messagebox.askyesnocancel(message="Do you want to save the actual configuration?",
                                           title="Warning")
        if answer is True:
            result = ConfigurationFilesFrame.button_export_configuration_clicked()
            if result is True:
                main_window.destroy()
            elif result is False:
                pass
        elif answer is False:
            main_window.destroy()
        elif answer is None:
            pass


# Setting window size.
main_window = tk.Tk()
app = Application(main_window)
'''
Mainloop is an endless loop of the window
The window will wait for any user interaction till we close it
'''
app.mainloop()
