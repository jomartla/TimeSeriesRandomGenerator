import tkinter as tk
from tkinter import ttk


class TrendFrame(ttk.Frame):

    # Global static parameters that can be accessed anywhere
    trend = 0
    trend_intensity = 0
    trend_randomness = 0
    trend_randomness_std = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        validate_float_command = (self.register(self.validate_float), '%P', '%W')

        # Label for trend
        self.label_trend = tk.Label(self,
                                    text="Trend",
                                    font=("Arial", 10))
        self.label_trend.grid(column=0, row=0, sticky="W", columnspan=3)

        # Radio button groups for trend
        self.radio_button_trend_value = tk.IntVar()
        self.radio_button_trend_value.set(TrendFrame.trend)

        self.radio_button_none_trend = tk.Radiobutton(self, text="None",
                                                      variable=self.radio_button_trend_value, value=1,
                                                      command=lambda:
                                                      self.save_parameters(
                                                          "radio_button_trend_value",
                                                          1))
        self.radio_button_none_trend.grid(column=0, row=1, sticky="W")

        self.radio_button_increasing_trend = tk.Radiobutton(self, text="Increasing",
                                                            variable=self.radio_button_trend_value, value=2,
                                                            command=lambda:
                                                            self.save_parameters(
                                                                "radio_button_trend_value",
                                                                2))
        self.radio_button_increasing_trend.grid(column=1, row=1, sticky="W")

        self.radio_button_decreasing_trend = tk.Radiobutton(self, text="Decreasing",
                                                            variable=self.radio_button_trend_value, value=3,
                                                            command=lambda:
                                                            self.save_parameters(
                                                                "radio_button_trend_value",
                                                                3))
        self.radio_button_decreasing_trend.grid(column=2, row=1, sticky="W")

        # Label for trend intensity
        self.label_trend_intensity = tk.Label(self, text="Trend intensity",
                                              font=("Arial", 10))
        self.label_trend_intensity.grid(column=0, row=2, sticky="W", columnspan=3)

        # Entry for trend intensity
        self.entry_trend_intensity = tk.Entry(self, name="entry_trend_intensity", width=10,
                                              validate="key", validatecommand=validate_float_command)
        self.entry_trend_intensity.insert(0, TrendFrame.trend_intensity)
        self.entry_trend_intensity.grid(column=0, row=3)

        # Label for trend randomness
        self.label_trend_randomness = tk.Label(self,
                                               text="Trend randomness",
                                               font=("Arial", 10))
        self.label_trend_randomness.grid(column=0, row=4, sticky="W", columnspan=3)

        # Radio button groups for trend randomness
        self.radio_button_trend_randomness_value = tk.IntVar()
        self.radio_button_trend_randomness_value.set(TrendFrame.trend_randomness)

        self.radio_button_trend_randomness_yes = tk.Radiobutton(self, text="Yes",
                                                                variable=self.radio_button_trend_randomness_value,
                                                                value=1,
                                                                command=lambda:
                                                                self.save_parameters(
                                                                    "radio_button_trend_randomness_value",
                                                                    1))
        self.radio_button_trend_randomness_yes.grid(column=0, row=5, sticky="W")

        self.radio_button_trend_randomness_no = tk.Radiobutton(self, text="No",
                                                               variable=self.radio_button_trend_randomness_value,
                                                               value=2,
                                                               command=lambda:
                                                               self.save_parameters(
                                                                   "radio_button_trend_randomness_value",
                                                                   2))
        self.radio_button_trend_randomness_no.grid(column=1, row=5, sticky="W")

        # Label for trend randomness standard deviation
        self.label_trend_randomness_std = tk.Label(self, text="Trend randomness standard deviation",
                                                   font=("Arial", 10))
        self.label_trend_randomness_std.grid(column=0, row=6, sticky="W", columnspan=3)

        # Entry for trend randomness standard deviation
        self.entry_trend_randomness_std = tk.Entry(self, name="entry_trend_randomness_std", width=10,
                                                   validate="key", validatecommand=validate_float_command)
        self.entry_trend_randomness_std.insert(0, TrendFrame.trend_randomness_std)
        self.entry_trend_randomness_std.grid(column=0, row=7)

    def update_layout(self):
        # Trend value
        self.radio_button_trend_value.set(TrendFrame.trend)
        # Trend intensity
        self.entry_trend_intensity.delete(0, len(self.entry_trend_intensity.get()))
        self.entry_trend_intensity.insert(0, TrendFrame.trend_intensity)
        # Trend randomness
        self.radio_button_trend_randomness_value.set(TrendFrame.trend_randomness)
        # Trend randomness standard deviation
        self.entry_trend_randomness_std.delete(0, len(self.entry_trend_randomness_std.get()))
        self.entry_trend_randomness_std.insert(0, TrendFrame.trend_randomness_std)

    # Function that save radio button parameters
    @staticmethod
    def save_parameters(name, value):
        # Trend Frame
        if name is "radio_button_trend_value":
            TrendFrame.trend = value
        elif name is "radio_button_trend_randomness_value":
            TrendFrame.trend_randomness = value

    # Function
    # noinspection PyUnusedLocal
    @staticmethod
    def validate_float(value_if_allowed, widget_name):
        try:
            float(value_if_allowed)
            # Trend Frame
            if "entry_trend_intensity" in widget_name:
                TrendFrame.trend_intensity = float(value_if_allowed)
            if "entry_trend_randomness_std" in widget_name:
                TrendFrame.trend_randomness_std = float(value_if_allowed)
            return True
        except ValueError:
            if value_if_allowed == '':
                return True
            else:
                return False
