from Frames.CSVFrame import CSVFrame
from Frames.Settings.TrendFrame import TrendFrame
from Frames.Settings.PeakValleyFrame import PeakValleyFrame
from Frames.Settings.PeriodicityFrame import PeriodicityFrame
from Frames.Settings.SeedFrame import SeedFrame

import numpy as np
import random
import math

csv_separator_dict = {
    1: ",",
    2: ";",
    3: "|"
}


# Check if a value is a positive, unsigned and integer number from tkinter import messagebox
def is_positive_unsigned_integer(s):
    if s.isdigit():
        return True
    else:
        return False


def check_integer(entry, error_text, parameter_name):
    value = entry.get()
    new_value = value

    if value:
        if not is_positive_unsigned_integer(value):
            error_text = error_text + parameter_name + " is not an integer" + "\n"
        else:
            new_value = int(value)

        if new_value != value:
            entry.delete(0, len(entry.get()))
            entry.insert(0, str(new_value))
    else:
        error_text = error_text + parameter_name + " is not given" + "\n"

    return new_value, error_text


# Check if a value is a float
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# Process to check if a number is a float and generate the error string
def check_float(entry, error_text, name_of_parameter):
    value = entry.get()
    new_value = value

    if value:
        new_value = value.replace(',', '.')
        if not is_float(new_value):
            error_text = error_text + name_of_parameter + " is not a valid number" + "\n"
        else:
            new_value = float(new_value)

        if new_value != value:
            entry.delete(0, len(entry.get()))
            entry.insert(0, str(new_value))
    else:
        error_text = error_text + name_of_parameter + " is not given" + "\n"

    return new_value, error_text


def replace_dot_by_comma(x):
    x = str(x).replace('.', ',')
    return x


def replace_comma_by_dot(x):
    x = str(x).replace(',', '.')
    return x


# Generate numbers with specific mean, standard deviation and trend
def generate_time_series(mean, std, number_of_values, seed_array, only_seed=False):

    # np.random.seed(0)
    samples = np.random.normal(loc=mean, scale=std, size=number_of_values)

    # First we generate some zero-mean samples, with the desired standard deviation
    actual_mean = np.mean(samples)

    # Then, subtract the sample mean from the samples so it is truly zero mean
    zero_mean_samples = samples - actual_mean

    zero_mean_std = np.std(zero_mean_samples)

    # Scale the samples so that the standard deviation is spot on
    if zero_mean_std != 0:
        scaled_samples = zero_mean_samples * (std / zero_mean_std)
    else:
        scaled_samples = zero_mean_samples

    # Add the the desired mean
    final_samples = scaled_samples + mean

    statistics_array = []
    names = []

    if CSVFrame.showing_statistics == 1:
        statistics_array.append("")
        names.append("Random array")
        statistics_array.extend(generate_statistics(final_samples, names))

    if not only_seed:
        # If trend
        if TrendFrame.trend != 1:

            trend_guide = np.zeros(number_of_values)

            if TrendFrame.trend == 2:
                trend_guide = np.linspace(0, TrendFrame.trend_intensity, number_of_values)
            elif TrendFrame.trend == 3:
                trend_guide = np.linspace(TrendFrame.trend_intensity, 0, number_of_values)

            if TrendFrame.trend_randomness == 1:
                added_randomness = np.random.normal(loc=0, scale=TrendFrame.trend_randomness_std,
                                                    size=number_of_values-2)
                added_randomness = np.insert(added_randomness, 0, 0)
                added_randomness = np.append(added_randomness, 0)
                trend_guide = trend_guide + added_randomness

            final_samples = final_samples + trend_guide

            if CSVFrame.showing_statistics == 1:
                statistics_array.extend(generate_statistics(trend_guide, ["Trend Guide"]))
                names.append("Trend")
                statistics_array.extend(generate_statistics(final_samples, names))

        # Peaks and Valleys
        if PeakValleyFrame.peaks_valleys != 1:
            peaks_valleys_array = generate_peaks_and_valleys(number_of_values, mean)
            final_samples = final_samples + peaks_valleys_array

            if CSVFrame.showing_statistics == 1:
                statistics_array.extend(generate_statistics(peaks_valleys_array, ["Peak Valley Guide"]))
                names.append("Peak & Valley")
                statistics_array.extend(generate_statistics(final_samples, names))

        # If periodicity
        if PeriodicityFrame.first_periodicity != 1:
            periodicity_array = []
            # Sin periodicity
            if PeriodicityFrame.first_periodicity == 2:
                # F(x) = A Sen ( Bx + [c] )
                values = np.arange(0, number_of_values)
                for value in values:
                    periodicity_array.append(PeriodicityFrame.first_amplitude *
                                             np.sin((2 * math.pi / (PeriodicityFrame.first_period - 1)) * value))

            # Cosine periodicity
            elif PeriodicityFrame.first_periodicity == 3:
                # F(x) = A Cos ( Bx + [c] )
                values = np.arange(0, number_of_values)
                for value in values:
                    periodicity_array.append(PeriodicityFrame.first_amplitude *
                                             np.cos((2 * math.pi / (PeriodicityFrame.first_period - 1)) * value))

            final_samples = final_samples + periodicity_array

            if CSVFrame.showing_statistics == 1:
                statistics_array.extend(generate_statistics(periodicity_array, ["First periodicity Guide"]))
                names.append("First periodicity")
                statistics_array.extend(generate_statistics(final_samples, names))

        # If periodicity
        if PeriodicityFrame.second_periodicity != 1:
            periodicity_array = []
            # Sin periodicity
            if PeriodicityFrame.second_periodicity == 2:
                # F(x) = A Sen ( Bx + [c] )
                values = np.arange(0, number_of_values)
                for value in values:
                    periodicity_array.append(PeriodicityFrame.second_amplitude *
                                                    np.sin((2 * math.pi / (PeriodicityFrame.second_period - 1)) * value))

            # Cosine periodicity
            elif PeriodicityFrame.second_periodicity == 3:
                # F(x) = A Cos ( Bx + [c] )
                values = np.arange(0, number_of_values)
                for value in values:
                    periodicity_array.append(PeriodicityFrame.second_amplitude *
                                             np.cos((2 * math.pi / (PeriodicityFrame.second_period - 1)) * value))

            final_samples = final_samples + periodicity_array

            if CSVFrame.showing_statistics == 1:
                statistics_array.extend(generate_statistics(periodicity_array, ["Second periodicity Guide"]))
                names.append("Second periodicity")
                statistics_array.extend(generate_statistics(final_samples, names))

        if SeedFrame.seed is 1:
            if len(seed_array) == len(final_samples):
                final_samples = final_samples + seed_array

            if CSVFrame.showing_statistics == 1:
                statistics_array.extend(generate_statistics(seed_array, ["Seed Added"]))
                names.append("Seed")
                statistics_array.extend(generate_statistics(final_samples, names))

        if CSVFrame.showing_statistics is 1:
            final_samples = np.append(final_samples, statistics_array)

    return final_samples


def decision(probability):
    return random.random() < probability


def generate_peaks_and_valleys(number_of_values, mean):
    # Generating an array of zeros
    zeros = np.zeros(number_of_values)

    for index in range(len(zeros)):
        # For this index, decide if there is a peak/valley or not
        if decision(PeakValleyFrame.pv_probability/100):
            peak_or_valley = np.zeros(number_of_values)

            flip_coin_recovery = -1

            # With or without recovery
            if PeakValleyFrame.pv_recovery == 3:
                # If the result is true, it would be with recovery
                # If the result is false, it would be without recovery
                flip_coin_recovery = decision(0.5)

            # With recovery
            if PeakValleyFrame.pv_recovery == 1 or (PeakValleyFrame.pv_recovery == 3 and flip_coin_recovery):
                random_selection = -1
                if PeakValleyFrame.pv_recovery_type == 4:
                    random_selection = random.random()

                if PeakValleyFrame.pv_recovery_type == 1 or 0 <= random_selection < 0.3333:
                    peak_or_valley = generate_peak_valley_with_recovery(mean, number_of_values,
                                                                        index,
                                                                        peak_duration=PeakValleyFrame.pv_recovery_units,
                                                                        beginning=True)
                elif PeakValleyFrame.pv_recovery_type == 2 or 0.3333 <= random_selection < 0.6666:
                    peak_or_valley = generate_peak_valley_with_recovery(mean, number_of_values,
                                                                        index,
                                                                        peak_duration=int(
                                                                            PeakValleyFrame.pv_recovery_units / 2),
                                                                        beginning=False) + \
                                     generate_peak_valley_with_recovery(mean, number_of_values,
                                                                        index + int(
                                                                            PeakValleyFrame.pv_recovery_units/2),
                                                                        peak_duration=int(
                                                                            PeakValleyFrame.pv_recovery_units/2),
                                                                        beginning=True)
                # The peak or valley should be at the end, so the values must reverse
                elif PeakValleyFrame.pv_recovery_type == 3 or 0.6666 <= random_selection <= 1:
                    peak_or_valley = generate_peak_valley_with_recovery(mean, number_of_values,
                                                                        index,
                                                                        peak_duration=PeakValleyFrame.pv_recovery_units,
                                                                        beginning=False)
            # Without recovery
            elif PeakValleyFrame.pv_recovery == 2 or (PeakValleyFrame.pv_recovery == 3 and not flip_coin_recovery):
                for n_index in range(index, number_of_values):
                    peak_or_valley[n_index] = peak_or_valley[n_index] + (mean * (PeakValleyFrame.pv_magnitude/100))

            flip_coin_peak_valley = -1

            if PeakValleyFrame.peaks_valleys == 4:
                # If the result is true, it would be a valley
                # If the result is false, it would be a peak
                flip_coin_peak_valley = decision(0.5)

            if PeakValleyFrame.peaks_valleys == 3 or (PeakValleyFrame.peaks_valleys == 4 and flip_coin_peak_valley):
                zeros = zeros - peak_or_valley
            else:
                zeros = zeros + peak_or_valley

    return zeros


# noinspection PyUnboundLocalVariable
def generate_peak_valley_with_recovery(mean, number_of_values, index, peak_duration, beginning=True):
    zeros = np.zeros(number_of_values)
    if index < number_of_values:
        zeros[index] = zeros[index] + (mean * (PeakValleyFrame.pv_magnitude / 100))
        recovery_per_step = (mean * (PeakValleyFrame.pv_magnitude / 100)) / peak_duration
    for step in range(1, peak_duration + 1):
        if (index + step) < number_of_values:
            zeros[index + step] = zeros[index + step] + (
                        mean * (PeakValleyFrame.pv_magnitude / 100) - (step * recovery_per_step))

    if not beginning:
        for step in range(0, int(peak_duration / 2) + 1):
            if (index + step) < number_of_values and \
                    (index + (peak_duration - step - 1)) < number_of_values:
                aux = zeros[index + step]
                zeros[index + step] = zeros[index + (peak_duration - step - 1)]
                zeros[index + (peak_duration - step - 1)] = aux

    return zeros


def generate_statistics(array, array_name):
    statistics = []
    final_name = ""

    aux = 0
    for name in array_name:
        if aux == 0:
            final_name = final_name + name
        else:
            final_name = final_name + " + " + name
        aux = aux + 1

    statistics.append(final_name + " std"),
    statistics.append(np.std(array).round(4))
    statistics.append(final_name + " mean")
    statistics.append(np.mean(array).round(4))

    return statistics
