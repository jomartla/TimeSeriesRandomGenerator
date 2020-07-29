from Frames.CSVFrame import CSVFrame
from Frames.Settings.TrendFrame import TrendFrame
from Frames.Settings.PeakValleyFrame import PeakValleyFrame
from Frames.Settings.PeriodicityFrame import PeriodicityFrame
from Frames.Settings.SeedFrame import SeedFrame
from Frames.Settings.MainFrame import MainFrame

import configparser
import os


class Parameters:

    # Instances of frames in execution time.
    # It allow us to update the entries, radio buttons, etc...
    main_frame = 0
    csv_frame = 0
    trend_frame = 0
    peak_valley_frame = 0
    periodicity_frame = 0
    seed_frame = 0

    def __init__(self):
        super().__init__()

    @staticmethod
    def read_parameters_from_conf_file(filename="", update_widgets=False):
        # Main Frame
        MainFrame.number_of_values = read_parameter_from_conf_ini("MAIN_FRAME", "NUMBER_OF_VALUES",
                                                                  int, filename)
        MainFrame.number_of_time_series = read_parameter_from_conf_ini("MAIN_FRAME", "NUMBER_OF_TIME_SERIES",
                                                                       int, filename)
        MainFrame.mean = read_parameter_from_conf_ini("MAIN_FRAME", "MEAN",
                                                      float, filename)
        MainFrame.standard_deviation = read_parameter_from_conf_ini("MAIN_FRAME", "STANDARD_DEVIATION",
                                                                    float, filename)
        MainFrame.standard_deviation_of_means = read_parameter_from_conf_ini("MAIN_FRAME",
                                                                             "STANDARD_DEVIATION_OF_MEANS",
                                                                             float, filename)
        # CSV Options
        CSVFrame.csv_separator = read_parameter_from_conf_ini("CSV_OPTIONS", "CSV_SEPARATOR",
                                                              int, filename)
        CSVFrame.decimal_separator = read_parameter_from_conf_ini("CSV_OPTIONS", "DECIMAL_SEPARATOR",
                                                                  int, filename)
        CSVFrame.displaying_mode = read_parameter_from_conf_ini("CSV_OPTIONS", "DISPLAYING_MODE",
                                                                int, filename)
        CSVFrame.showing_statistics = read_parameter_from_conf_ini("CSV_OPTIONS", "SHOWING_STATISTICS",
                                                                   int, filename)

        # Trend Options
        TrendFrame.trend = read_parameter_from_conf_ini("TREND_OPTIONS", "TREND",
                                                        int, filename)
        TrendFrame.trend_intensity = read_parameter_from_conf_ini("TREND_OPTIONS", "TREND_INTENSITY",
                                                                  float, filename)
        TrendFrame.trend_randomness = read_parameter_from_conf_ini("TREND_OPTIONS", "TREND_RANDOMNESS",
                                                                   int, filename)
        TrendFrame.trend_randomness_std = read_parameter_from_conf_ini("TREND_OPTIONS", "TREND_RANDOMNESS_STD",
                                                                       float, filename)
        # Peak & Valley Options
        PeakValleyFrame.peaks_valleys = read_parameter_from_conf_ini("PEAK_VALLEY_OPTIONS", "PEAK_VALLEY_OPTION",
                                                                     int, filename)
        PeakValleyFrame.pv_magnitude = read_parameter_from_conf_ini("PEAK_VALLEY_OPTIONS", "MAGNITUDE",
                                                                    float, filename)
        PeakValleyFrame.pv_probability = read_parameter_from_conf_ini("PEAK_VALLEY_OPTIONS", "PROBABILITY",
                                                                      float, filename)
        PeakValleyFrame.pv_recovery = read_parameter_from_conf_ini("PEAK_VALLEY_OPTIONS", "RECOVERY",
                                                                   int, filename)
        PeakValleyFrame.pv_recovery_units = read_parameter_from_conf_ini("PEAK_VALLEY_OPTIONS", "RECOVERY_TIME_UNITS",
                                                                         int, filename)
        PeakValleyFrame.pv_recovery_type = read_parameter_from_conf_ini("PEAK_VALLEY_OPTIONS", "RECOVERY_TYPE",
                                                                        int, filename)

        # Periodicity Options
        PeriodicityFrame.first_periodicity = read_parameter_from_conf_ini("PERIODICITY_OPTIONS", "FIRST_PERIODICITY",
                                                                          int, filename)
        PeriodicityFrame.first_amplitude = read_parameter_from_conf_ini("PERIODICITY_OPTIONS", "FIRST_AMPLITUDE",
                                                                        float, filename)
        PeriodicityFrame.first_period = read_parameter_from_conf_ini("PERIODICITY_OPTIONS", "FIRST_PERIOD",
                                                                     float, filename)

        # Periodicity Options
        PeriodicityFrame.second_periodicity = read_parameter_from_conf_ini("PERIODICITY_OPTIONS", "SECOND_PERIODICITY",
                                                                           int, filename)
        PeriodicityFrame.second_amplitude = read_parameter_from_conf_ini("PERIODICITY_OPTIONS", "SECOND_AMPLITUDE",
                                                                         float, filename)
        PeriodicityFrame.second_period = read_parameter_from_conf_ini("PERIODICITY_OPTIONS", "SECOND_PERIOD",
                                                                      float, filename)

        # Seed Options
        SeedFrame.seed = read_parameter_from_conf_ini("SEED_OPTIONS", "SEED",
                                                      int, filename)
        SeedFrame.seed_filename = read_parameter_from_conf_ini("SEED_OPTIONS", "SEED_FILENAME",
                                                               "string", filename)

        if filename != "" or update_widgets:
            Parameters.main_frame.update_layout()
            Parameters.csv_frame.update_layout()
            Parameters.trend_frame.update_layout()
            Parameters.peak_valley_frame.update_layout()
            Parameters.periodicity_frame.update_layout()
            Parameters.seed_frame.update_layout()

    @staticmethod
    def write_parameters_in_conf_file(filename=""):
        # Main Frame
        write_parameter_in_conf_ini("MAIN_FRAME", "NUMBER_OF_VALUES",
                                    MainFrame.number_of_values, filename)
        write_parameter_in_conf_ini("MAIN_FRAME", "NUMBER_OF_TIME_SERIES",
                                    MainFrame.number_of_time_series, filename)
        write_parameter_in_conf_ini("MAIN_FRAME", "MEAN",
                                    MainFrame.mean, filename)
        write_parameter_in_conf_ini("MAIN_FRAME", "STANDARD_DEVIATION",
                                    MainFrame.standard_deviation, filename)
        write_parameter_in_conf_ini("MAIN_FRAME", "STANDARD_DEVIATION_OF_MEANS",
                                    MainFrame.standard_deviation_of_means, filename)
        # CSV Options
        write_parameter_in_conf_ini("CSV_OPTIONS", "CSV_SEPARATOR",
                                    CSVFrame.csv_separator, filename)
        write_parameter_in_conf_ini("CSV_OPTIONS", "DECIMAL_SEPARATOR",
                                    CSVFrame.decimal_separator, filename)
        write_parameter_in_conf_ini("CSV_OPTIONS", "DISPLAYING_MODE",
                                    CSVFrame.displaying_mode, filename)
        write_parameter_in_conf_ini("CSV_OPTIONS", "SHOWING_STATISTICS",
                                    CSVFrame.showing_statistics, filename)

        # Trend Options
        write_parameter_in_conf_ini("TREND_OPTIONS", "TREND",
                                    TrendFrame.trend, filename)
        write_parameter_in_conf_ini("TREND_OPTIONS", "TREND_INTENSITY",
                                    TrendFrame.trend_intensity, filename)
        write_parameter_in_conf_ini("TREND_OPTIONS", "TREND_RANDOMNESS",
                                    TrendFrame.trend_randomness, filename)
        write_parameter_in_conf_ini("TREND_OPTIONS", "TREND_RANDOMNESS_STD",
                                    TrendFrame.trend_randomness_std, filename)
        # Peak & Valley Options
        write_parameter_in_conf_ini("PEAK_VALLEY_OPTIONS", "PEAK_VALLEY_OPTION",
                                    PeakValleyFrame.peaks_valleys, filename)
        write_parameter_in_conf_ini("PEAK_VALLEY_OPTIONS", "MAGNITUDE",
                                    PeakValleyFrame.pv_magnitude, filename)
        write_parameter_in_conf_ini("PEAK_VALLEY_OPTIONS", "PROBABILITY",
                                    PeakValleyFrame.pv_probability, filename)
        write_parameter_in_conf_ini("PEAK_VALLEY_OPTIONS", "RECOVERY",
                                    PeakValleyFrame.pv_recovery, filename)
        write_parameter_in_conf_ini("PEAK_VALLEY_OPTIONS", "RECOVERY_TIME_UNITS",
                                    PeakValleyFrame.pv_recovery_units, filename)
        write_parameter_in_conf_ini("PEAK_VALLEY_OPTIONS", "RECOVERY_TYPE",
                                    PeakValleyFrame.pv_recovery_type, filename)
        # First periodicity Options
        write_parameter_in_conf_ini("PERIODICITY_OPTIONS", "FIRST_PERIODICITY",
                                    PeriodicityFrame.first_periodicity, filename)
        write_parameter_in_conf_ini("PERIODICITY_OPTIONS", "FIRST_AMPLITUDE",
                                    PeriodicityFrame.first_amplitude, filename)
        write_parameter_in_conf_ini("PERIODICITY_OPTIONS", "FIRST_PERIOD",
                                    PeriodicityFrame.first_period, filename)

        # Second periodicity Options
        write_parameter_in_conf_ini("PERIODICITY_OPTIONS", "SECOND_PERIODICITY",
                                    PeriodicityFrame.second_periodicity, filename)
        write_parameter_in_conf_ini("PERIODICITY_OPTIONS", "SECOND_AMPLITUDE",
                                    PeriodicityFrame.second_amplitude, filename)
        write_parameter_in_conf_ini("PERIODICITY_OPTIONS", "SECOND_PERIOD",
                                    PeriodicityFrame.second_period, filename)

        # Seed Options
        write_parameter_in_conf_ini("SEED_OPTIONS", "SEED",
                                    SeedFrame.seed, filename)
        write_parameter_in_conf_ini("SEED_OPTIONS", "SEED_FILENAME",
                                    SeedFrame.seed_filename, filename)


# Read parameter from conf.ini
def read_parameter_from_conf_ini(parameter, sub_parameter, variable_type, filename=""):
    config = configparser.ConfigParser()

    if filename == "":
        currentDirectory = os.getcwd()
        filename = currentDirectory + '/conf.ini'

    config.read(filename)

    if variable_type is int:
        try:
            new_value = config.getint(parameter, sub_parameter)
        except (configparser.NoSectionError, configparser.NoOptionError):
            new_value = 0
    elif variable_type is float:
        try:
            new_value = config.getfloat(parameter, sub_parameter)
        except (configparser.NoSectionError, configparser.NoOptionError):
            new_value = 0.0
    elif variable_type is bool:
        try:
            new_value = config.getboolean(parameter, sub_parameter)
        except (configparser.NoSectionError, configparser.NoOptionError):
            new_value = False
    else:
        try:
            new_value = config.get(parameter, sub_parameter)
        except (configparser.NoSectionError, configparser.NoOptionError):
            new_value = 0

    return new_value


# Read parameter from conf.ini
def write_parameter_in_conf_ini(parameter, sub_parameter, new_value, filename=""):
    # Initialize the config parser
    config = configparser.RawConfigParser()

    # If there is no filename, the default one is selected
    if filename == "":
        currentDirectory = os.getcwd()
        filename = currentDirectory + '/conf.ini'

    config.read(filename)

    try:
        config.set(parameter, sub_parameter, str(new_value))
    except configparser.NoSectionError:
        # Create non-existent section
        config.add_section(parameter)
        config.set(parameter, sub_parameter, str(new_value))

    # Writing our configuration file to 'example.ini'
    with open(filename, 'w') as configfile:
        config.write(configfile)
