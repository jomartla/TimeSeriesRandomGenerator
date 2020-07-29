import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from Frames.CSVFrame import CSVFrame

import numpy as np
import csv


class SeedFrame(ttk.Frame):

    # Global static parameters that can be accessed anywhere
    seed = 0
    seed_filename = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.csv_separator_dict = {
            1: ",",
            2: ";",
            3: "|"
        }

        # Label for seed
        self.label_seed = tk.Label(self, text="Seed",
                                   font=("Arial", 10))
        self.label_seed.grid(column=0, row=0, sticky="W", columnspan=3)

        # Radio button groups for seed
        self.radio_button_seed_value = tk.IntVar()
        self.radio_button_seed_value.set(SeedFrame.seed)

        self.radio_button_no_seed = tk.Radiobutton(self, text="Yes",
                                                   variable=self.radio_button_seed_value, value=1,
                                                   command=lambda:
                                                   self.save_parameters(
                                                       "radio_button_seed_value",
                                                       1))
        self.radio_button_no_seed.grid(column=0, row=1, sticky="W")

        self.radio_button_seed_no = tk.Radiobutton(self, text="No",
                                                   variable=self.radio_button_seed_value,
                                                   value=2,
                                                   command=lambda:
                                                   self.save_parameters(
                                                       "radio_button_seed_value",
                                                       2))
        self.radio_button_seed_no.grid(column=1, row=1, sticky="W")

        # Label for seed filename
        self.label_seed_filename = tk.Label(self, text="Seed Filename",
                                            font=("Arial", 10))
        self.label_seed_filename.grid(column=0, row=2, sticky="W", columnspan=3)

        # Entry for trend intensity
        self.entry_seed_filename = tk.Entry(self, name="entry_seed_filename", width=20)
        self.entry_seed_filename.insert(0, SeedFrame.seed_filename)
        self.entry_seed_filename.configure(state='disabled')
        self.entry_seed_filename.grid(column=0, row=3, columnspan=2)

        # Button search seed
        self.button_search_seed = tk.Button(self, text="Search seed", command=self.button_search_seed_clicked)
        self.button_search_seed.grid(column=2, row=3)

        # Horizontal separator
        self.separator = ttk.Separator(self, orient=tk.HORIZONTAL)
        self.separator.grid(column=0, row=4, columnspan=3, ipadx=125, pady=[10, 10])

        # Variable for seed number of values text
        self.label_seed_number_of_values_text = tk.StringVar()
        self.label_seed_number_of_values_text.set("")

        # Label for seed number of values
        self.label_seed_number_of_values = tk.Label(self, textvariable=self.label_seed_number_of_values_text,
                                                    font=("Arial", 10))
        self.label_seed_number_of_values.grid(column=0, row=5, sticky="W", columnspan=3)

        # Variable for seed mean text
        self.label_seed_mean_text = tk.StringVar()
        self.label_seed_mean_text.set("")

        # Label for seed mean
        self.label_seed_mean = tk.Label(self, textvariable=self.label_seed_mean_text,
                                        font=("Arial", 10))
        self.label_seed_mean.grid(column=0, row=6, sticky="W", columnspan=3)

        # Variable for seed std text
        self.label_seed_std_text = tk.StringVar()
        self.label_seed_std_text.set("")

        # Label for seed standard deviation
        self.label_seed_std = tk.Label(self, textvariable=self.label_seed_std_text,
                                       font=("Arial", 10))
        self.label_seed_std.grid(column=0, row=7, sticky="W", columnspan=3)

        # Update information values
        self.update_seed_information()

    def update_layout(self):
        # Seed
        self.radio_button_seed_value.set(SeedFrame.seed)
        # Seed filename
        self.entry_seed_filename.configure(state='normal')
        self.entry_seed_filename.delete(0, len(self.entry_seed_filename.get()))
        self.entry_seed_filename.insert(0, SeedFrame.seed_filename)
        self.entry_seed_filename.configure(state='disabled')

        self.update_seed_information()

    # Update the information about the seed
    def update_seed_information(self):
        # Reading seed properties
        try:
            with open(SeedFrame.seed_filename, 'r', newline='') as file:
                reader = csv.reader(file,
                                    delimiter=self.csv_separator_dict[CSVFrame.csv_separator])

                seed_array = []
                line = next(reader)
                try:
                    for number in line:
                        if number == "":
                            break
                        if CSVFrame.decimal_separator == 1:
                            number = str(number).replace(',', '.')
                        seed_array.append(float(number))

                    # Update text
                    self.label_seed_number_of_values_text.set("Number of values: " + str(len(seed_array)))
                    self.label_seed_mean_text.set("Mean: " + str(np.mean(seed_array).round(4)))
                    self.label_seed_std_text.set("Standard deviation: " + str(np.std(seed_array).round(4)))
                except ValueError:
                    messagebox.showwarning("Warning",
                                           "Seed has a different format than the values specified in CSV settings. " +
                                           "It can not be used.")
                    self.label_seed_number_of_values_text.set("Number of values: ? ")
                    self.label_seed_mean_text.set("Mean: ? ")
                    self.label_seed_std_text.set("Standard deviation: ? ")
        except FileNotFoundError:
            self.label_seed_number_of_values_text.set("Number of values: ? ")
            self.label_seed_mean_text.set("Mean: ? ")
            self.label_seed_std_text.set("Standard deviation: ? ")

            SeedFrame.seed_filename = ""
            SeedFrame.seed = 2
            # Seed
            self.radio_button_seed_value.set(SeedFrame.seed)
            # Seed filename
            self.entry_seed_filename.configure(state='normal')
            self.entry_seed_filename.delete(0, len(self.entry_seed_filename.get()))
            self.entry_seed_filename.insert(0, SeedFrame.seed_filename)
            self.entry_seed_filename.configure(state='disabled')

    # Function that save radio button parameters
    @staticmethod
    def save_parameters(name, value):
        # CSV Frame
        if name is "radio_button_seed_value":
            SeedFrame.seed = value

    def button_search_seed_clicked(self):
        # Selecting seed
        seed_filename = filedialog.askopenfilename(title="Select seed",
                                                   filetypes=[("csv", "*.csv")],
                                                   defaultextension=".csv")

        if seed_filename is None or seed_filename is "":
            messagebox.showerror("Error", "File error")
            return False
        else:
            self.entry_seed_filename.configure(state='normal')
            self.entry_seed_filename.delete(0, len(self.entry_seed_filename.get()))
            self.entry_seed_filename.insert(0, seed_filename)
            self.entry_seed_filename.configure(state='disabled')

            SeedFrame.seed_filename = seed_filename

            self.update_seed_information()
