# Analyzing-River-Thames-Water-Levels
Apply your data manipulation skills to time series data on water levels of the River Thames. 

# Description:
Working with time series data is essential to enable the analysis of trends, patterns, and seasonality in data over time, facilitating forecasting, anomaly detection, and decision-making.

In this project, you’ll use your pandas data manipulation skills to analyze time series data tracking the tide levels of the Thames River over many years.

# Project Instructions
Analyze Thames River tidal data to track changes in high-tide and low-tide frequency over time.

The data is in the data/10-11_London_Bridge.txt file.

Load, manipulate, and prepare the data to create new structures and names that might benefit your analysis.

Find the mean, median, and interquartile range for high- and low-tide data and save them as two separate pandas Series.

Calculate the annual percentage of days with very high tide levels (90th percentile of high tide days) for each year and store the results as floats in a two-column DataFrame with the index reset.

Calculate the same percentage for low-tide days (below the 10th percentile) and store the results in the same way.

Create a dictionary named solution with a summary of your data analysis, with these key-value pairs:

{high_statistics: high-tide stats, low_statistics: low-tide stats, very_high_ratio: high-tide ratio data, very_low_ratio: low-tide ratio data}

# Analyzing River Thames Water Levels
Time series data is everywhere, from watching your stock portfolio to monitoring climate change, and even live-tracking as local cases of a virus become a global pandemic. In this project, you’ll work with a time series that tracks the tide levels of the Thames River. You’ll first load the data and inspect it data visually, and then perform calculations on the dataset to generate some summary statistics. You’ll end by reducing the time series to its component attributes and analyzing them. 

The original dataset is available from the British Oceanographic Data Center.

Here's a map of the locations of the tidal meters along the River Thames in London.

![image](https://github.com/user-attachments/assets/c15bb81a-2f83-4fad-bd91-e636ae59554d)


The provided datasets are in the `data` folder in this workspace. For this project, you will work with one of these files, `10-11_London_Bridge.txt`, which contains comma separated values for water levels in the Thames River at the London Bridge. After you've finished the project, you can use your same code to analyze data from the other files (at other spots in the UK where tidal data is collected) if you'd like. 

The TXT file contains data for three variables, described in the table below. 

| Variable Name | Description | Format |
| ------------- | ----------- | ------ |
| Date and time | Date and time of measurement to GMT. Note the tide gauge is accurate to one minute. | dd/mm/yyyy hh:mm:ss |
| Water level | High or low water level measured by tide meter. Tide gauges are accurate to 1 centimetre. | metres (Admiralty Chart Datum (CD), Ordnance Datum Newlyn (ODN or Trinity High Water (THW)) | 
| Flag | High water flag = 1, low water flag = 0 | Categorical (0 or 1) |

