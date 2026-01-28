# energy-consumption-analysis
Analyze electricity usage to optimize energy costs (Python + NumPy + Pandas + Matplotlib)

# Energy Consumption Analysis (Python)

## Project Overview
This project analyzes electricity consumption data to understand
how energy is used over time and to identify peak usage periods.
The goal is to help reduce energy cost using data analysis.

## Dataset Description
The dataset contains uncleaned smart meter data collected every 15 minutes.
It includes missing values and abnormal readings to simulate real-time data.

### Columns:
- timestamp : Date and time of reading
- meter_id : Electricity meter ID
- voltage : Voltage level
- current : Current flow
- power_kw : Power consumption in kilowatts
- temperature_c : Temperature in Celsius

## Tools Used
- Python
- Pandas
- NumPy
- Matplotlib

## Steps Followed
1. Loaded uncleaned electricity usage data
2. Converted timestamp into datetime format
3. Handled missing values using forward fill
4. Removed outliers using quantile method
5. Created time-based features (hour, day, month)
6. Analyzed peak electricity usage hours
7. Calculated daily and monthly energy consumption
8. Used rolling average to understand consumption trend
9. Visualized results using line graphs

## Results
- Identified peak electricity usage hours
- Observed daily and monthly consumption patterns
- Rolling average helped understand overall energy trend

## Conclusion
This analysis helps identify high energy usage periods and provides
insights to optimize electricity consumption and reduce energy costs.
