from tkinter import filedialog, messagebox
import tkinter as tk
from tkinter import ttk

import sklearn.cluster as sk_c

from Frames.VisualizationFrame import VisualizationFrame

import numpy as np
import csv
import pandas as pd


class MainFrame(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.left_frame = tk.Frame(self)

        # ListBox for showing the csv selected
        self.listbox_for_file_names = tk.Listbox(self.left_frame, width=50, height=10)
        self.listbox_for_file_names.grid(row=0, column=0, rowspan=5, padx=[0, 15], sticky="NW")

        # Button to add files
        self.button_add_files = tk.Button(self.left_frame, text="Add files", width=10,
                                          command=self.button_add_files_clicked)
        self.button_add_files.grid(row=0, column=1, pady=[0, 15], sticky='NW')

        # Button to remove file
        self.button_remove_file = tk.Button(self.left_frame, text="Remove file", width=10,
                                            command=self.button_remove_file_clicked)
        self.button_remove_file.grid(row=1, column=1, pady=[0, 15], sticky='NW')

        # Button to remove all files
        self.button_remove_all_files = tk.Button(self.left_frame, text="Remove files", width=10,
                                                 command=self.button_remove_all_files_clicked)
        self.button_remove_all_files.grid(row=2, column=1, pady=[0, 15], sticky='NW')

        # Button to visualize a file
        self.button_visualize_file = tk.Button(self.left_frame, text="Visualize file", width=10,
                                               command=self.button_visualize_file_clicked)
        self.button_visualize_file.grid(row=3, column=1, pady=[0, 15], sticky='NW')

        # Button to run
        self.button_run = tk.Button(self.left_frame, text="Run", width=10,
                                    command=self.button_run_clicked)
        self.button_run.grid(row=4, column=1, pady=[15, 0], sticky="SW")

        self.left_frame.grid(row=0, column=0, padx=15, pady=15, sticky="N")

        # Vertical separator

        self.vertical_separator = tk.ttk.Separator(self, orient=tk.VERTICAL)
        self.vertical_separator.grid(column=1, row=0, pady=[15, 15], sticky='ns')

        # Right frame
        self.right_frame = tk.Frame(self)

        # Label for number of coefficients
        self.label_number_coefficients = tk.Label(self.right_frame, text="Number of coefficients")
        self.label_number_coefficients.grid(column=0, row=0, sticky='W')

        # Spinbox for selecting the coefficients
        self.spinbox_coefficients = tk.Spinbox(self.right_frame, from_=0, to=1000)
        self.spinbox_coefficients.delete(0, len(self.spinbox_coefficients.get()))
        self.spinbox_coefficients.insert(0, 4)
        self.spinbox_coefficients.grid(column=0, row=1, sticky='W')

        # Label for number of centroids for clustering
        self.label_number_groups = tk.Label(self.right_frame,
                                            text="Number of clusters")
        self.label_number_groups.grid(column=0, row=2, sticky='W')

        # Spinbox for selecting the coefficients
        self.spinbox_groups = tk.Spinbox(self.right_frame, from_=0, to=1000)
        self.spinbox_groups.delete(0, len(self.spinbox_groups.get()))
        self.spinbox_groups.insert(0, 4)
        self.spinbox_groups.grid(column=0, row=3, sticky='W')

        self.right_frame.grid(row=0, column=2, padx=5, pady=15, sticky="N")

    # Function that run button triggers
    def button_add_files_clicked(self):

        csv_filenames = filedialog.askopenfilenames(title="Select files",
                                                    filetypes=[("csv", "*.csv")],
                                                    defaultextension=".csv")

        csv_filenames = list(csv_filenames)

        for csv_filename in csv_filenames:
            if csv_filename is None or csv_filename is "":
                messagebox.showerror("Error", "File error")
                return

        for csv_filename in csv_filenames:
            self.listbox_for_file_names.insert(self.listbox_for_file_names.size(),
                                               csv_filename)

    # Function that run button triggers
    def button_remove_file_clicked(self):
        if self.listbox_for_file_names.curselection():
            self.listbox_for_file_names.delete(self.listbox_for_file_names.curselection())

    # Function that run button triggers
    def button_remove_all_files_clicked(self):
        self.listbox_for_file_names.delete(0, tk.END)

    # Function to visualize a file button triggers
    def button_visualize_file_clicked(self):

        csv_filename = ""
        visualization_matrix = []
        dft_matrix = []
        event_num = 0

        if self.listbox_for_file_names.curselection():
            csv_filename = self.listbox_for_file_names.get(self.listbox_for_file_names.curselection())
        else:
            return

        with open(csv_filename, newline='') as file:
            reader = csv.reader(file, delimiter=';')

            for row in reader:
                # Find the index of the empty value before statistics
                try:
                    # If this value exists, we get the values before the index
                    index = row.index("")
                    row = row[0:index]
                except ValueError:
                    # If not exists, nothing happens
                    pass

                # Transform commas to dots if needed before the transformation
                row = np.core.defchararray.replace(row, ',', '.')

                # Convert to floats
                row = np.array(row).astype(np.float)

                # Append the results to the visualization matrix
                visualization_matrix.append(row)

                # Number of values
                number_of_values = len(row)

                fft = np.fft.rfft(row)

                coefficients = int(self.spinbox_coefficients.get())
            
                dft_matrix.append(np.fft.irfft(fft[0:coefficients], number_of_values))

            # Activate the visualization frame
            visualization_frame = VisualizationFrame()

            visualization_frame.visualization_matrix = visualization_matrix
            visualization_frame.dft_matrix = dft_matrix
            visualization_frame.event_num = event_num

            visualization_frame.update_time_series_visualization(perform_pan=True)
            visualization_frame.visualization_frame.grid(row=0, column=0)

    # Function that run button triggers
    def button_run_clicked(self):

        final_dataframe = []
        coefficients = 0

        for item in enumerate(self.listbox_for_file_names.get(0, tk.END)):
            dft_matrix = []

            csv_filename = item[1]

            with open(csv_filename, newline='') as file:
                reader = csv.reader(file, delimiter=';')

                counter = 1

                for row in reader:
                    # Find the index of the empty value before statistics
                    try:
                        # If this value exists, we get the values before the index
                        index = row.index("")
                        row = row[0:index]
                    except ValueError:
                        # If not exists, nothing happens
                        pass

                    # Transform commas to dots if needed before the transformation
                    row = np.core.defchararray.replace(row, ',', '.')

                    # Convert to floats
                    row = np.array(row).astype(np.float)

                    fft = np.fft.rfft(row)

                    coefficients_list = []

                    coefficients = int(self.spinbox_coefficients.get())

                    aux = 1
                    for complex_number in fft:
                        if aux <= coefficients:
                            coefficients_list.append(float(complex_number.real))
                            coefficients_list.append(float(complex_number.imag))
                        else:
                            break
                        aux = aux + 1

                    coefficients_list.insert(0, counter)
                    coefficients_list.insert(0, csv_filename)

                    dft_matrix.append(coefficients_list)

                    counter = counter + 1

            final_dataframe.extend(dft_matrix)

        final_dataframe = pd.DataFrame(final_dataframe)

        k_means = sk_c.KMeans(n_clusters=int(self.spinbox_groups.get()))
        k_means = k_means.fit(final_dataframe.iloc[:, 2:])
        final_dataframe.insert(2, "Cluster", k_means.predict(final_dataframe.iloc[:, 2:]) + 1)

        column_names = ["File", "Time series", "Cluster"]

        for i in range(0, coefficients):
            column_names.append("Coefficient " + str(i+1) + " (Real)")
            column_names.append("Coefficient " + str(i+1) + " (Imaginary)")

        final_dataframe.columns = column_names

        final_dataframe.iloc[:, 3:] = final_dataframe.iloc[:, 3:].round(8).astype(str)

        final_dataframe.iloc[:, 3:] = final_dataframe.iloc[:, 3:].apply(lambda x: x.str.replace('.', ','))

        # Saving the file
        csv_result = filedialog.asksaveasfilename(title="Save results",
                                                  filetypes=[("csv", "*.csv")],
                                                  defaultextension=".csv")

        if csv_result is None or csv_result is "":
            messagebox.showerror("Error", "File error")
            return

        final_dataframe.to_csv(csv_result, index=False, sep=';', encoding='utf-8')
