import tkinter as tk
from tkinter import ttk


class CSVFrame(ttk.Frame):

    # Global static parameters that can be accessed anywhere
    csv_separator = 0
    decimal_separator = 0
    displaying_mode = 0
    showing_statistics = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Label for csv separator
        self.label_csv_separator = tk.Label(self,
                                            text="CSV separator",
                                            font=("Arial", 10))
        self.label_csv_separator.grid(column=0, row=0, sticky="W", columnspan=3)

        # Radio button groups for csv separator
        self.radio_button_csv_separator_value = tk.IntVar()
        self.radio_button_csv_separator_value.set(CSVFrame.csv_separator)

        self.radio_button_comma = tk.Radiobutton(self, text="Comma",
                                                 variable=self.radio_button_csv_separator_value, value=1,
                                                 command=lambda:
                                                 self.save_parameters(
                                                     "radio_button_csv_separator_value",
                                                     1))
        self.radio_button_comma.grid(column=0, row=1, sticky="W")

        self.radio_button_semicolon = tk.Radiobutton(self, text="Semicolon",
                                                     variable=self.radio_button_csv_separator_value, value=2,
                                                     command=lambda:
                                                     self.save_parameters(
                                                         "radio_button_csv_separator_value",
                                                         2))
        self.radio_button_semicolon.grid(column=1, row=1, sticky="W")

        self.radio_button_vertical_slash = tk.Radiobutton(self, text="Vertical slash",
                                                          variable=self.radio_button_csv_separator_value, value=3,
                                                          command=lambda:
                                                          self.save_parameters(
                                                              "radio_button_csv_separator_value",
                                                              3))
        self.radio_button_vertical_slash.grid(column=2, row=1, sticky="W")

        # Label for csv decimal separator
        self.label_decimal_separator = tk.Label(self,
                                                text="Decimal separator",
                                                font=("Arial", 10))
        self.label_decimal_separator.grid(column=0, row=2, sticky="W", columnspan=3)

        # Radio button groups for decimal separator
        self.radio_button_decimal_separator_value = tk.IntVar()
        self.radio_button_decimal_separator_value.set(CSVFrame.decimal_separator)

        self.radio_button_comma = tk.Radiobutton(self, text="Comma",
                                                 variable=self.radio_button_decimal_separator_value, value=1,
                                                 command=lambda:
                                                 self.save_parameters(
                                                     "radio_button_decimal_separator_value",
                                                     1))
        self.radio_button_comma.grid(column=0, row=3, sticky="W")

        self.radio_button_dot = tk.Radiobutton(self, text="Dot",
                                               variable=self.radio_button_decimal_separator_value, value=2,
                                               command=lambda:
                                               self.save_parameters(
                                                   "radio_button_decimal_separator_value",
                                                   2))
        self.radio_button_dot.grid(column=1, row=3, sticky="W")

        # Label for csv displaying mode (rows or columns)
        self.label_displaying_mode = tk.Label(self,
                                              text="T.S. displaying mode",
                                              font=("Arial", 10))
        self.label_displaying_mode.grid(column=0, row=4, sticky="W", columnspan=3)

        # Radio button groups for displaying mode
        self.radio_button_displaying_mode_value = tk.IntVar()
        self.radio_button_displaying_mode_value.set(CSVFrame.displaying_mode)

        self.radio_button_ts_in_rows = tk.Radiobutton(self, text="Rows",
                                                      variable=self.radio_button_displaying_mode_value, value=1,
                                                      command=lambda:
                                                      self.save_parameters(
                                                          "radio_button_displaying_mode_value",
                                                          1))
        self.radio_button_ts_in_rows.grid(column=0, row=5, sticky="W")

        self.radio_button_ts_in_columns = tk.Radiobutton(self, text="Columns",
                                                         variable=self.radio_button_displaying_mode_value, value=2,
                                                         command=lambda:
                                                         self.save_parameters(
                                                             "radio_button_displaying_mode_value",
                                                             2))
        self.radio_button_ts_in_columns.grid(column=1, row=5, sticky="W")

        # Label for statistics
        self.label_statistics = tk.Label(self,
                                         text="Statistics",
                                         font=("Arial", 10))
        self.label_statistics.grid(column=0, row=6, sticky="W", columnspan=3)

        # Radio button groups for showing statistics
        self.radio_button_showing_statistics_value = tk.IntVar()
        self.radio_button_showing_statistics_value.set(CSVFrame.showing_statistics)

        self.radio_button_show_statistics = tk.Radiobutton(self, text="Yes",
                                                           variable=self.radio_button_showing_statistics_value, value=1,
                                                           command=lambda:
                                                           self.save_parameters(
                                                               "radio_button_showing_statistics_value",
                                                               1))
        self.radio_button_show_statistics.grid(column=0, row=7, sticky="W")

        self.radio_button_do_not_show_statistics = tk.Radiobutton(self, text="No",
                                                                  variable=self.radio_button_showing_statistics_value,
                                                                  value=2,
                                                                  command=lambda:
                                                                  self.save_parameters(
                                                                      "radio_button_showing_statistics_value",
                                                                      2))
        self.radio_button_do_not_show_statistics.grid(column=1, row=7, sticky="W")

    def update_layout(self):
        # CSV separator
        self.radio_button_csv_separator_value.set(CSVFrame.csv_separator)
        # Decimal separator
        self.radio_button_decimal_separator_value.set(CSVFrame.decimal_separator)
        # Displaying mode
        self.radio_button_displaying_mode_value.set(CSVFrame.displaying_mode)
        # Statistics
        self.radio_button_showing_statistics_value.set(CSVFrame.showing_statistics)

    # Function that save radio button parameters
    @staticmethod
    def save_parameters(name, value):
        # CSV Frame
        if name is "radio_button_csv_separator_value":
            CSVFrame.csv_separator = value
        elif name is "radio_button_decimal_separator_value":
            CSVFrame.decimal_separator = value
        elif name is "radio_button_displaying_mode_value":
            CSVFrame.displaying_mode = value
        elif name is "radio_button_showing_statistics_value":
            CSVFrame.showing_statistics = value
