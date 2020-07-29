from tkinter import filedialog, messagebox
import tkinter as tk
from tkinter import ttk

from Frames.VisualizationFrame import VisualizationFrame
from Frames.Settings.SeedFrame import SeedFrame

import numpy as np
import csv

from utilities import check_integer, csv_separator_dict
from utilities import check_float, generate_time_series, replace_dot_by_comma

from Frames.CSVFrame import CSVFrame


class MainFrame(ttk.Frame):
    number_of_values = 0
    number_of_time_series = 0
    mean = 0
    standard_deviation = 0
    standard_deviation_of_means = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        validate_int_command = (self.register(self.validate_int),
                                '%P', '%W')
        validate_float_command = (self.register(self.validate_float),
                                  '%P', '%W')

        self.parameters_frame = tk.Frame(self)

        # Label for number of values
        self.label_number_of_values = tk.Label(self.parameters_frame, text="Number of values",
                                               font=("Arial", 12))
        self.label_number_of_values.grid(column=0, row=0)

        # Entry for number of values
        self.entry_number_of_values = tk.Entry(self.parameters_frame, name="entry_number_of_values", width=10,
                                               validate="key", validatecommand=validate_int_command)
        self.entry_number_of_values.insert(0, MainFrame.number_of_values)
        self.entry_number_of_values.grid(column=1, row=0)

        # Label for number of time series
        self.label_number_of_time_series = tk.Label(self.parameters_frame, text="Number of time series",
                                                    font=("Arial", 12))
        self.label_number_of_time_series.grid(column=0, row=1)

        # Entry for number of time series
        self.entry_number_of_time_series = tk.Entry(self.parameters_frame, name="entry_number_of_time_series", width=10,
                                                    validate="key", validatecommand=validate_int_command)
        self.entry_number_of_time_series.insert(0, MainFrame.number_of_time_series)
        self.entry_number_of_time_series.grid(column=1, row=1)

        # Label for mean
        self.label_mean = tk.Label(self.parameters_frame, text="Mean",
                                   font=("Arial", 12))
        self.label_mean.grid(column=0, row=2)

        # Entry for mean
        self.entry_mean = tk.Entry(self.parameters_frame, name="entry_mean", width=10,
                                   validate="key", validatecommand=validate_float_command)
        self.entry_mean.insert(0, MainFrame.mean)
        self.entry_mean.grid(column=1, row=2)

        # Label for standard deviation
        self.label_standard_deviation = tk.Label(self.parameters_frame, text="Standard deviation",
                                                 font=("Arial", 12))
        self.label_standard_deviation.grid(column=0, row=3)

        # Entry for standard deviation
        self.entry_standard_deviation = tk.Entry(self.parameters_frame, name="entry_standard_deviation", width=10,
                                                 validate="key", validatecommand=validate_float_command)
        self.entry_standard_deviation.insert(0, MainFrame.standard_deviation)
        self.entry_standard_deviation.grid(column=1, row=3)

        # Label for standard deviation of the means
        self.label_standard_deviation_of_means = tk.Label(self.parameters_frame, text="Standard deviation (of means)",
                                                          font=("Arial", 12))
        self.label_standard_deviation_of_means.grid(column=0, row=4)

        # Entry for standard deviation of the means
        self.entry_standard_deviation_of_means = tk.Entry(self.parameters_frame,
                                                          name="entry_standard_deviation_of_means", width=10,
                                                          validate="key", validatecommand=validate_float_command)
        self.entry_standard_deviation_of_means.insert(0, MainFrame.standard_deviation_of_means)
        self.entry_standard_deviation_of_means.grid(column=1, row=4)

        # Button to run the program
        self.button_run = tk.Button(self.parameters_frame, text="Run", command=self.button_run_clicked)
        self.button_run.grid(column=0, row=5)

        self.parameters_frame.grid(row=0, column=0)

    # Function that run button triggers
    def button_run_clicked(self):
        error_text = ""

        # Get the values from the entries
        number_of_values, error_text = check_integer(self.entry_number_of_values,
                                                     error_text, "Number of values")

        number_of_time_series, error_text = check_integer(self.entry_number_of_time_series,
                                                          error_text,
                                                          "Number of time series")

        mean, error_text = check_float(self.entry_mean,
                                       error_text,
                                       "Mean")

        standard_deviation, error_text = check_float(self.entry_standard_deviation,
                                                     error_text,
                                                     "Standard deviation")

        standard_deviation_of_means, error_text = check_float(self.entry_standard_deviation_of_means,
                                                              error_text,
                                                              "Standard deviation of means")

        if error_text != "":
            messagebox.showerror("Error", error_text)
        else:
            # Saving the file
            csv_filename = filedialog.asksaveasfilename(title="Save file",
                                                        filetypes=[("csv", "*.csv")],
                                                        defaultextension=".csv")

            if csv_filename is None or csv_filename is "":
                messagebox.showerror("Error", "File error")
                return

            means_for_time_series = \
                generate_time_series(mean=mean,
                                     std=standard_deviation_of_means,
                                     number_of_values=number_of_time_series,
                                     seed_array=[],
                                     only_seed=True)

            list_to_write = []
            visualization_matrix = []
            event_num = 0
            seed_array = []

            if SeedFrame.seed is 1:

                try:
                    with open(SeedFrame.seed_filename, newline='') as csv_file:
                        seed_data = csv.reader(csv_file, delimiter=csv_separator_dict[CSVFrame.csv_separator])
                        row = next(seed_data)
                        for number in row:
                            if number == "":
                                break
                            if CSVFrame.decimal_separator == 1:
                                number = str(number).replace(',', '.')
                            seed_array.append(float(number))
                    if number_of_values != len(seed_array):
                        messagebox.showwarning("Warning", "Seed has a different number of values than specified. " +
                                               "So it is not added to the result.")
                except ValueError:
                    messagebox.showwarning("Warning",
                                           "Seed has a different format than the values specified in CSV settings. " +
                                           "It can not be used.")

            for mean_for_time_series in means_for_time_series:
                time_series = generate_time_series(mean=mean_for_time_series, std=standard_deviation,
                                                   number_of_values=number_of_values, seed_array=seed_array)

                # Add the time series generated to the visualization
                visualization_matrix.append(np.array(time_series[0:number_of_values]).astype(np.float))

                if CSVFrame.decimal_separator == 1:
                    time_series = np.array([replace_dot_by_comma(x) for x in time_series])
                    list_to_write.append(time_series)
                elif CSVFrame.decimal_separator == 2:
                    list_to_write.append(time_series)

            # Activate the visualization frame
            visualization_frame = VisualizationFrame()

            visualization_frame.visualization_matrix = visualization_matrix
            visualization_frame.event_num = event_num

            visualization_frame.update_time_series_visualization(perform_pan=True)
            visualization_frame.visualization_frame.grid(row=0, column=0)

            list_to_write = np.array(list_to_write)

            if CSVFrame.displaying_mode == 2:
                list_to_write = list_to_write.T

            with open(csv_filename, 'w', newline='') as outfile:
                writer = csv.writer(outfile,
                                    delimiter=csv_separator_dict[CSVFrame.csv_separator])

                writer.writerows(list_to_write)

    # Update layout with global static variables of the class
    def update_layout(self):
        # Number of values
        self.entry_number_of_values.delete(0, len(self.entry_number_of_values.get()))
        self.entry_number_of_values.insert(0, MainFrame.number_of_values)
        # Number of time series
        self.entry_number_of_time_series.delete(0, len(self.entry_number_of_time_series.get()))
        self.entry_number_of_time_series.insert(0, MainFrame.number_of_time_series)
        # Mean
        self.entry_mean.delete(0, len(self.entry_mean.get()))
        self.entry_mean.insert(0, MainFrame.mean)
        # Standard deviation
        self.entry_standard_deviation.delete(0, len(self.entry_standard_deviation.get()))
        self.entry_standard_deviation.insert(0, MainFrame.standard_deviation)
        # Standard deviation of means
        self.entry_standard_deviation_of_means.delete(0, len(self.entry_standard_deviation_of_means.get()))
        self.entry_standard_deviation_of_means.insert(0, MainFrame.standard_deviation_of_means)

    # Function
    @staticmethod
    def validate_int(value_if_allowed, widget_name):
        try:
            int(value_if_allowed)
            # Main Frame
            if "entry_number_of_values" in widget_name:
                MainFrame.number_of_values = int(value_if_allowed)
            if "entry_number_of_time_series" in widget_name:
                MainFrame.number_of_time_series = int(value_if_allowed)
            return True
        except ValueError:
            if value_if_allowed == '':
                return True
            else:
                return False

    # Function
    @staticmethod
    def validate_float(value_if_allowed, widget_name):
        try:
            float(value_if_allowed)
            # Main Frame
            if "entry_mean" in widget_name:
                MainFrame.mean = float(value_if_allowed)
            if "entry_standard_deviation" in widget_name:
                MainFrame.standard_deviation = float(value_if_allowed)
            if "entry_standard_deviation_of_means" in widget_name:
                MainFrame.standard_deviation_of_means = float(value_if_allowed)
            return True
        except ValueError:
            if value_if_allowed == '':
                return True
            else:
                return False
