# Time Series Random Generator - Master's thesis

## Introduction

A time series is an ordered sequence of values. This data type appears in many real-life domains, as the result of measuring continuously any kind of variable. For example, in medicine, seismology, finances…

Lots of projects have been carried out in the field of time series prediction or analysis. There are many attempts to predict the stock market in financial companies. Also, in medicine the patient cardiograms are analysed using data mining techniques for finding anomalies, etc.

Due to its many applications, this is a field studied for many years. However, it has acquired a new dimension with the arrival of COVID-19, and many projects have been started trying to help in the current situation.

For this master’s thesis, the objective is twofold. First, a time series random generator must be designed and developed. Given some parameters, it can generate synthetic random time series. These parameters are related to time series properties such as trend, periodicity, the appearance of events like peaks or valleys...

Secondly, another application will be designed and developed. It will use data mining techniques to group the different synthetic generated time series.

These techniques will consist of performing Fourier transformations on the time series, and using the coefficients obtained as inputs for a clustering algorithm. Thus, it will be important as a proper data mining tool but also as a means to prove the correct functioning of the time series random generator and its many functionalities.

## Test the applications

The **FunctionalExecutables** folder contains the Windows executables along a configuration file. The applications are self-contained and ready to use, but the configuration file needs to be in the same folder than the executables.

## Source code

The applications are contained in folders **App_TimeSeriesRandomGenerator** and **App_DataMiningApplication**. They are independent of each other and must be developed separately. I used PyCharm as an IDE.

## The report

The PDF file is the thesis report that explains step by step how everything has been developed.
