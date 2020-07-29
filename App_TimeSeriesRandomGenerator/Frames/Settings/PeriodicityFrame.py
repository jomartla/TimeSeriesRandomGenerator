import tkinter as tk
from tkinter import ttk


class PeriodicityFrame(ttk.Frame):

    # Global static parameters that can be accessed anywhere
    first_periodicity = 0
    first_amplitude = 0
    first_period = 0

    second_periodicity = 0
    second_amplitude = 0
    second_period = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Variable to validate dynamically the entry text updates
        validate_float_command = (self.register(self.validate_float), '%P', '%W')

        self.first_periodicity_frame = tk.LabelFrame(self, text="First", font=("Arial", 10))

        # Label for first periodicity
        self.label_first_periodicity = tk.Label(self.first_periodicity_frame,
                                                text="Periodicity",
                                                font=("Arial", 10))
        self.label_first_periodicity.grid(column=0, row=0, sticky="W", columnspan=3)

        # Radio button groups for first periodicity
        self.radio_button_first_periodicity_value = tk.IntVar()
        self.radio_button_first_periodicity_value.set(PeriodicityFrame.first_periodicity)

        self.radio_button_none_first_periodicity = tk.Radiobutton(self.first_periodicity_frame, text="None",
                                                                  variable=self.radio_button_first_periodicity_value,
                                                                  value=1,
                                                                  command=lambda:
                                                                  self.save_parameters(
                                                                      "radio_button_first_periodicity_value",
                                                                      1))
        self.radio_button_none_first_periodicity.grid(column=0, row=1, sticky="W")

        self.radio_button_sin_first_periodicity = tk.Radiobutton(self.first_periodicity_frame, text="Sine",
                                                                 variable=self.radio_button_first_periodicity_value,
                                                                 value=2,
                                                                 command=lambda:
                                                                 self.save_parameters(
                                                                     "radio_button_first_periodicity_value",
                                                                     2))
        self.radio_button_sin_first_periodicity.grid(column=1, row=1, sticky="W")

        self.radio_button_cosine_first_periodicity = tk.Radiobutton(self.first_periodicity_frame, text="Cosine",
                                                                    variable=self.radio_button_first_periodicity_value,
                                                                    value=3,
                                                                    command=lambda:
                                                                    self.save_parameters(
                                                                        "radio_button_first_periodicity_value",
                                                                        3))
        self.radio_button_cosine_first_periodicity.grid(column=2, row=1, sticky="W")

        # Label for first amplitude
        self.label_first_amplitude = tk.Label(self.first_periodicity_frame, text="Amplitude",
                                              font=("Arial", 10))
        self.label_first_amplitude.grid(column=0, row=2, sticky="W")

        # Entry for first amplitude
        self.entry_first_amplitude = tk.Entry(self.first_periodicity_frame, name="entry_first_amplitude", width=10,
                                              validate="key", validatecommand=validate_float_command)
        self.entry_first_amplitude.insert(0, PeriodicityFrame.first_amplitude)
        self.entry_first_amplitude.grid(column=0, row=3)

        # Label for first period
        self.label_first_period = tk.Label(self.first_periodicity_frame, text="Period",
                                           font=("Arial", 10))
        self.label_first_period.grid(column=0, row=4, sticky="W")

        # Entry for first period
        self.entry_first_period = tk.Entry(self.first_periodicity_frame, name="entry_first_period", width=10,
                                           validate="key", validatecommand=validate_float_command)
        self.entry_first_period.insert(0, PeriodicityFrame.first_period)
        self.entry_first_period.grid(column=0, row=5)

        self.first_periodicity_frame.grid(column=0, row=0, padx=10, pady=2.5)

        self.second_periodicity_frame = tk.LabelFrame(self, text="Second",
                                                      font=("Arial", 10))

        # Label for second periodicity
        self.label_second_periodicity = tk.Label(self.second_periodicity_frame,
                                                 text="Periodicity",
                                                 font=("Arial", 10))
        self.label_second_periodicity.grid(column=0, row=0, sticky="W", columnspan=3)

        # Radio button groups for second periodicity
        self.radio_button_second_periodicity_value = tk.IntVar()
        self.radio_button_second_periodicity_value.set(PeriodicityFrame.second_periodicity)

        self.radio_button_none_second_periodicity = tk.Radiobutton(self.second_periodicity_frame, text="None",
                                                                   variable=self.radio_button_second_periodicity_value,
                                                                   value=1,
                                                                   command=lambda:
                                                                   self.save_parameters(
                                                                       "radio_button_second_periodicity_value",
                                                                       1))
        self.radio_button_none_second_periodicity.grid(column=0, row=1, sticky="W")

        self.radio_button_sin_second_periodicity = tk.Radiobutton(self.second_periodicity_frame, text="Sine",
                                                                  variable=self.radio_button_second_periodicity_value,
                                                                  value=2,
                                                                  command=lambda:
                                                                  self.save_parameters(
                                                                      "radio_button_second_periodicity_value",
                                                                      2))
        self.radio_button_sin_second_periodicity.grid(column=1, row=1, sticky="W")

        self.radio_button_cosine_second_periodicity = tk.Radiobutton(self.second_periodicity_frame, text="Cosine",
                                                                     variable=self.radio_button_second_periodicity_value,
                                                                     value=3,
                                                                     command=lambda:
                                                                     self.save_parameters(
                                                                         "radio_button_second_periodicity_value",
                                                                         3))
        self.radio_button_cosine_second_periodicity.grid(column=2, row=1, sticky="W")

        # Label for second amplitude
        self.label_second_amplitude = tk.Label(self.second_periodicity_frame, text="Amplitude",
                                               font=("Arial", 10))
        self.label_second_amplitude.grid(column=0, row=2, sticky="W")

        # Entry for second amplitude
        self.entry_second_amplitude = tk.Entry(self.second_periodicity_frame, name="entry_second_amplitude", width=10,
                                               validate="key", validatecommand=validate_float_command)
        self.entry_second_amplitude.insert(0, PeriodicityFrame.second_amplitude)
        self.entry_second_amplitude.grid(column=0, row=3)

        # Label for second period
        self.label_second_period = tk.Label(self.second_periodicity_frame, text="Period",
                                            font=("Arial", 10))
        self.label_second_period.grid(column=0, row=4, sticky="W")

        # Entry for second period
        self.entry_second_period = tk.Entry(self.second_periodicity_frame, name="entry_second_period", width=10,
                                            validate="key", validatecommand=validate_float_command)
        self.entry_second_period.insert(0, PeriodicityFrame.second_period)
        self.entry_second_period.grid(column=0, row=5)

        self.second_periodicity_frame.grid(column=0, row=1, padx=10, pady=2.5)

    def update_layout(self):
        # First periodicity value
        self.radio_button_first_periodicity_value.set(PeriodicityFrame.first_periodicity)
        # First amplitude value
        self.entry_first_amplitude.delete(0, len(self.entry_first_amplitude.get()))
        self.entry_first_amplitude.insert(0, PeriodicityFrame.first_amplitude)
        # First period value
        self.entry_first_period.delete(0, len(self.entry_first_period.get()))
        self.entry_first_period.insert(0, PeriodicityFrame.first_period)

        # Second periodicity value
        self.radio_button_second_periodicity_value.set(PeriodicityFrame.second_periodicity)
        # Second amplitude value
        self.entry_second_amplitude.delete(0, len(self.entry_second_amplitude.get()))
        self.entry_second_amplitude.insert(0, PeriodicityFrame.second_amplitude)
        # Second period value
        self.entry_second_period.delete(0, len(self.entry_second_period.get()))
        self.entry_second_period.insert(0, PeriodicityFrame.second_period)

    # Function that save radio button parameters
    @staticmethod
    def save_parameters(name, value):
        # First periodicity
        if name is "radio_button_first_periodicity_value":
            PeriodicityFrame.first_periodicity = value
        if name is "radio_button_second_periodicity_value":
            PeriodicityFrame.second_periodicity = value

    # Function
    # noinspection PyUnusedLocal
    @staticmethod
    def validate_float(value_if_allowed, widget_name):
        try:
            float(value_if_allowed)
            # First periodicity
            if "entry_first_amplitude" in widget_name:
                PeriodicityFrame.first_amplitude = float(value_if_allowed)
            if "entry_first_period" in widget_name:
                PeriodicityFrame.first_period = float(value_if_allowed)
            # Second periodicity
            if "entry_second_amplitude" in widget_name:
                PeriodicityFrame.second_amplitude = float(value_if_allowed)
            if "entry_second_period" in widget_name:
                PeriodicityFrame.second_period = float(value_if_allowed)
            return True
        except ValueError:
            if value_if_allowed == '':
                return True
            else:
                return False
