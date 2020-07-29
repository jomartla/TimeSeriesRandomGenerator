from tkinter import ttk

from Frames.Settings.MainFrame import MainFrame
from Frames.Settings.TrendFrame import TrendFrame
from Frames.Settings.PeakValleyFrame import PeakValleyFrame
from Frames.Settings.PeriodicityFrame import PeriodicityFrame
from Frames.Settings.SeedFrame import SeedFrame
from Frames.Settings.Parameters import Parameters


class SettingsFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create tabs panel
        self.notebook = ttk.Notebook(self)

        self.mainframe = MainFrame(self.notebook)
        self.notebook.add(
            self.mainframe, text="Main")
        Parameters.main_frame = self.mainframe

        self.trend_frame = TrendFrame(self.notebook)
        self.notebook.add(
            self.trend_frame, text="Trend", padding=10)
        Parameters.trend_frame = self.trend_frame

        self.peak_valley_frame = PeakValleyFrame(self.notebook)
        self.notebook.add(
            self.peak_valley_frame, text="Peaks & Valleys", padding=10)
        Parameters.peak_valley_frame = self.peak_valley_frame

        self.periodicity_frame = PeriodicityFrame(self.notebook)
        self.notebook.add(
            self.periodicity_frame, text="Periodicity", padding=10)
        Parameters.periodicity_frame = self.periodicity_frame

        self.seed_frame = SeedFrame(self.notebook)
        self.notebook.add(
            self.seed_frame, text="Seed", padding=10)
        Parameters.seed_frame = self.seed_frame

        self.notebook.pack()
