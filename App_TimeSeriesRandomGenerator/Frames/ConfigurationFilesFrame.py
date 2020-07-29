import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from Frames.Settings.Parameters import Parameters


class ConfigurationFilesFrame(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Label for default configuration
        self.label_default_configuration = tk.Label(self,
                                                    text="Default configuration",
                                                    font=("Arial", 10))
        self.label_default_configuration.grid(column=0, row=0, sticky="W", columnspan=3)

        # Button to save actual configuration as default
        self.button_save_configuration_as_default = tk.Button(self, text="Save actual configuration as default",
                                                              command=self.button_save_configuration_as_default_clicked)
        self.button_save_configuration_as_default.grid(column=0, row=1, sticky="W")

        # Button to save actual configuration as default
        self.button_restore_default_configuration = tk.Button(self, text="Restore default configuration",
                                                              command=self.button_restore_default_configuration_clicked)
        self.button_restore_default_configuration.grid(column=0, row=2, sticky="W")

        # Label for import/export configuration files
        self.label_import_export_configuration_files = tk.Label(self,
                                                                text="\nImport/Export configuration files",
                                                                font=("Arial", 10))
        self.label_import_export_configuration_files.grid(column=0, row=3, sticky="W", columnspan=3)

        # Button to save_actual_configuration
        self.button_export_configuration = tk.Button(self, text="Export configuration to file",
                                                     command=self.button_export_configuration_clicked)
        self.button_export_configuration.grid(column=0, row=4, sticky="W")

        # Button to upload a configuration file
        self.button_import_configuration = tk.Button(self, text="Import configuration from file",
                                                     command=self.button_import_configuration_clicked)
        self.button_import_configuration.grid(column=0, row=5, sticky="W")

    @staticmethod
    def button_save_configuration_as_default_clicked():
        Parameters.write_parameters_in_conf_file()

    @staticmethod
    def button_restore_default_configuration_clicked():
        Parameters.read_parameters_from_conf_file(update_widgets=True)

    @staticmethod
    def button_export_configuration_clicked():
        # Saving the file
        conf_filename = filedialog.asksaveasfilename(title="Export configuration",
                                                     filetypes=[("ini", "*.ini")],
                                                     defaultextension=".ini")

        if conf_filename is None or conf_filename is "":
            messagebox.showerror("Error", "File error")
            return False
        else:
            Parameters.write_parameters_in_conf_file(filename=conf_filename)
            return True

    @staticmethod
    def button_import_configuration_clicked():
        # Saving the file
        conf_filename = filedialog.askopenfilename(title="Import configuration",
                                                   filetypes=[("ini", "*.ini")],
                                                   defaultextension=".ini")

        if conf_filename is None or conf_filename is "":
            messagebox.showerror("Error", "File error")
            return
        else:
            Parameters.read_parameters_from_conf_file(filename=conf_filename)
