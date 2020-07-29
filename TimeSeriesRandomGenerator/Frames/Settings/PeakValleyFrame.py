import tkinter as tk
from tkinter import ttk


class PeakValleyFrame(ttk.Frame):
    # Global static parameters that can be accessed anywhere
    peaks_valleys = 0
    pv_magnitude = 0
    pv_probability = 0
    pv_recovery = 0
    pv_recovery_units = 0
    pv_recovery_type = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Variable to validate dynamically the entry text updates
        validate_float_command = (self.register(self.validate_float), '%P', '%W')
        validate_int_command = (self.register(self.validate_int), '%P', '%W')

        # Label for peaks and valleys
        self.label_peaks_valleys = tk.Label(self,
                                            text="Peaks & Valleys",
                                            font=("Arial", 10))
        self.label_peaks_valleys.grid(column=0, row=0, sticky="W", columnspan=4)

        # Radio button groups for peaks and valleys
        self.radio_button_peaks_valleys_value = tk.IntVar()
        self.radio_button_peaks_valleys_value.set(PeakValleyFrame.peaks_valleys)

        self.radio_button_none_peak_or_valleys = tk.Radiobutton(self, text="None",
                                                                variable=self.radio_button_peaks_valleys_value, value=1,
                                                                command=lambda:
                                                                self.save_parameters(
                                                                    "radio_button_peaks_valleys_value",
                                                                    1))
        self.radio_button_none_peak_or_valleys.grid(column=0, row=1, sticky="W", columnspan=4)

        self.radio_button_only_peak = tk.Radiobutton(self, text="Peak",
                                                     variable=self.radio_button_peaks_valleys_value, value=2,
                                                     command=lambda:
                                                     self.save_parameters(
                                                         "radio_button_peaks_valleys_value",
                                                         2))
        self.radio_button_only_peak.grid(column=1, row=1, sticky="W")

        self.radio_button_only_valley = tk.Radiobutton(self, text="Valley",
                                                       variable=self.radio_button_peaks_valleys_value, value=3,
                                                       command=lambda:
                                                       self.save_parameters(
                                                           "radio_button_peaks_valleys_value",
                                                           3))
        self.radio_button_only_valley.grid(column=2, row=1, sticky="W")

        self.radio_button_both_valley_peak = tk.Radiobutton(self, text="Both",
                                                            variable=self.radio_button_peaks_valleys_value, value=4,
                                                            command=lambda:
                                                            self.save_parameters(
                                                                "radio_button_peaks_valleys_value",
                                                                4))
        self.radio_button_both_valley_peak.grid(column=3, row=1, sticky="W")

        # Label for peaks or valleys magnitude
        self.label_magnitude = tk.Label(self, text="Magnitude over the mean (%)",
                                        font=("Arial", 10))
        self.label_magnitude.grid(column=0, row=2, sticky="W", columnspan=4)

        # Entry for peaks or valleys magnitude
        self.entry_magnitude = tk.Entry(self, name="entry_magnitude", width=10,
                                        validate="key", validatecommand=validate_float_command)
        self.entry_magnitude.insert(0, PeakValleyFrame.pv_magnitude)
        self.entry_magnitude.grid(column=0, row=3, sticky="W")

        # Label for peaks or valleys probability
        self.label_probability = tk.Label(self, text="Probability of occurrence (%)",
                                          font=("Arial", 10))
        self.label_probability.grid(column=0, row=4, sticky="W", columnspan=4)

        # Entry for peaks or valleys probability
        self.entry_probability = tk.Entry(self, name="entry_probability", width=10,
                                          validate="key", validatecommand=validate_float_command)
        self.entry_probability.insert(0, PeakValleyFrame.pv_probability)
        self.entry_probability.grid(column=0, row=5, sticky="W")

        # Label for Recovery
        self.label_recovery = tk.Label(self,
                                       text="Recovery",
                                       font=("Arial", 10))
        self.label_recovery.grid(column=0, row=6, sticky="W", columnspan=4)

        # Radio button groups for recovery
        self.radio_button_recovery_value = tk.IntVar()
        self.radio_button_recovery_value.set(PeakValleyFrame.pv_recovery)

        self.radio_button_recovery_yes = tk.Radiobutton(self, text="Yes",
                                                        variable=self.radio_button_recovery_value, value=1,
                                                        command=lambda:
                                                        self.save_parameters(
                                                            "radio_button_recovery_value",
                                                            1))
        self.radio_button_recovery_yes.grid(column=0, row=7, sticky="W", columnspan=4)

        self.radio_button_recovery_no = tk.Radiobutton(self, text="No",
                                                       variable=self.radio_button_recovery_value, value=2,
                                                       command=lambda:
                                                       self.save_parameters(
                                                           "radio_button_recovery_value",
                                                           2))
        self.radio_button_recovery_no.grid(column=1, row=7, sticky="W")

        self.radio_button_recovery_both = tk.Radiobutton(self, text="Both",
                                                         variable=self.radio_button_recovery_value, value=3,
                                                         command=lambda:
                                                         self.save_parameters(
                                                             "radio_button_recovery_value",
                                                             3))
        self.radio_button_recovery_both.grid(column=2, row=7, sticky="W")

        # If recovery, in days
        self.label_recovery_in_time_units = tk.Label(self, text="Duration in time units",
                                                     font=("Arial", 10))
        self.label_recovery_in_time_units.grid(column=0, row=8, sticky="W", columnspan=4)

        # Entry for time units of the recovery
        self.entry_recovery_in_time_units = tk.Entry(self, name="entry_recovery_in_time_units", width=10,
                                                     validate="key", validatecommand=validate_int_command)
        self.entry_recovery_in_time_units.insert(0, PeakValleyFrame.pv_recovery_units)
        self.entry_recovery_in_time_units.grid(column=0, row=9, sticky="W")

        # Label for peaks and valleys type
        self.label_recovery_type = tk.Label(self,
                                            text="Peak position in recovery",
                                            font=("Arial", 10))
        self.label_recovery_type.grid(column=0, row=10, sticky="W", columnspan=4)

        # Radio button groups for recovery type
        self.radio_button_recovery_type_value = tk.IntVar()
        self.radio_button_recovery_type_value.set(PeakValleyFrame.pv_recovery_type)

        self.radio_button_recovery_type_beginning = tk.Radiobutton(self, text="Beginning",
                                                                   variable=self.radio_button_recovery_type_value,
                                                                   value=1,
                                                                   command=lambda:
                                                                   self.save_parameters(
                                                                       "radio_button_recovery_type_value",
                                                                       1))
        self.radio_button_recovery_type_beginning.grid(column=0, row=11, sticky="W")

        self.radio_button_recovery_type_middle = tk.Radiobutton(self, text="Middle",
                                                                variable=self.radio_button_recovery_type_value,
                                                                value=2,
                                                                command=lambda:
                                                                self.save_parameters(
                                                                    "radio_button_recovery_type_value",
                                                                    2))
        self.radio_button_recovery_type_middle.grid(column=1, row=11, sticky="W")

        self.radio_button_recovery_type_end = tk.Radiobutton(self, text="End",
                                                             variable=self.radio_button_recovery_type_value,
                                                             value=3,
                                                             command=lambda:
                                                             self.save_parameters(
                                                                 "radio_button_recovery_type_value",
                                                                 3))
        self.radio_button_recovery_type_end.grid(column=2, row=11, sticky="W")

        self.radio_button_recovery_type_all = tk.Radiobutton(self, text="All",
                                                             variable=self.radio_button_recovery_type_value,
                                                             value=4,
                                                             command=lambda:
                                                             self.save_parameters(
                                                                 "radio_button_recovery_type_value",
                                                                 4))
        self.radio_button_recovery_type_all.grid(column=3, row=11, sticky="W")

    # noinspection DuplicatedCode
    def update_layout(self):
        # Peaks and valleys
        self.radio_button_peaks_valleys_value.set(PeakValleyFrame.peaks_valleys)
        # Magnitude
        self.entry_magnitude.delete(0, len(self.entry_magnitude.get()))
        self.entry_magnitude.insert(0, PeakValleyFrame.pv_magnitude)
        # Probability
        self.entry_probability.delete(0, len(self.entry_probability.get()))
        self.entry_probability.insert(0, PeakValleyFrame.pv_probability)
        # Recovery
        self.radio_button_recovery_value.set(PeakValleyFrame.pv_recovery)
        # Entry for time units of the recovery
        self.entry_recovery_in_time_units.delete(0, len(self.entry_recovery_in_time_units.get()))
        self.entry_recovery_in_time_units.insert(0, PeakValleyFrame.pv_recovery_units)
        # Recovery
        self.radio_button_recovery_type_value.set(PeakValleyFrame.pv_recovery_type)

    # Function that save radio button parameters
    @staticmethod
    def save_parameters(name, value):
        # Peak and Valley
        if name is "radio_button_peaks_valleys_value":
            PeakValleyFrame.peaks_valleys = value
        elif name is "radio_button_recovery_value":
            PeakValleyFrame.pv_recovery = value
        elif name is "radio_button_recovery_type_value":
            PeakValleyFrame.pv_recovery_type = value

    # Function
    # noinspection PyUnusedLocal
    @staticmethod
    def validate_int(value_if_allowed, widget_name):
        try:
            int(value_if_allowed)
            if "entry_recovery_in_time_units" in widget_name:
                PeakValleyFrame.pv_recovery_units = int(value_if_allowed)
            return True
        except ValueError:
            if value_if_allowed == '':
                return True
            else:
                return False

    # Function
    # noinspection PyUnusedLocal
    @staticmethod
    def validate_float(value_if_allowed, widget_name):
        try:
            float(value_if_allowed)
            # Peak & Valley Frame
            if "entry_magnitude" in widget_name:
                PeakValleyFrame.pv_magnitude = float(value_if_allowed)
            if "entry_probability" in widget_name:
                PeakValleyFrame.pv_probability = float(value_if_allowed)
            return True
        except ValueError:
            if value_if_allowed == '':
                return True
            else:
                return False
