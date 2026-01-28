# ==============================
# STEP 1: Import libraries
# ==============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ==============================
# STEP 2: Load dataset
# ==============================
df = pd.read_csv("energy_consumption_uncleaned.csv")

print("First 5 rows:")
print(df.head())

print("\n--- BASIC DATA INFO ---")
df.info()

print("\n--- FULL DATA DESCRIPTION ---")
print(df.describe())

print("\n--- POWER USAGE DESCRIPTION ---")
print(df["power_kw"].describe())

avg_power = np.mean(df["power_kw"])
print("Average power usage:", avg_power)


# ==============================
# STEP 3: Convert timestamp
# ==============================
df["timestamp"] = pd.to_datetime(df["timestamp"])


# ==============================
# STEP 4: Sort by time
# ==============================
df = df.sort_values("timestamp")


# ==============================
# STEP 5: Handle missing values (NEW WAY ✅)
# ==============================
df = df.ffill()


# ==============================
# STEP 6: Remove outliers using quantile
# ==============================
Q1 = df["power_kw"].quantile(0.25)
Q3 = df["power_kw"].quantile(0.75)

df = df[(df["power_kw"] >= Q1) & (df["power_kw"] <= Q3)]


# ==============================
# STEP 7: Create time features
# ==============================
df["hour"] = df["timestamp"].dt.hour
df["day"] = df["timestamp"].dt.day
df["month"] = df["timestamp"].dt.month


# ==============================
# STEP 8: Peak usage analysis
# ==============================
hourly_usage = df.groupby("hour")["power_kw"].mean()

print("\nAverage power usage by hour:")
print(hourly_usage)


# ==============================
# STEP 9: Daily consumption
# ==============================
daily_usage = df.resample("D", on="timestamp")["power_kw"].sum()

print("\nDaily power usage:")
print(daily_usage.head())


# ==============================
# STEP 10: Monthly consumption (NEW WAY ✅)
# ==============================
monthly_usage = df.resample("ME", on="timestamp")["power_kw"].sum()

print("\nMonthly power usage:")
print(monthly_usage)


# ==============================
# STEP 11: Rolling average
# ==============================
df["rolling_avg"] = df["power_kw"].rolling(10).mean()


# ==============================
# STEP 12: Graphs
# ==============================

plt.figure()
hourly_usage.plot()
plt.title("Average Power Usage by Hour")
plt.xlabel("Hour")
plt.ylabel("Power (kW)")
plt.show()

plt.figure()
daily_usage.plot()
plt.title("Daily Power Consumption")
plt.xlabel("Date")
plt.ylabel("Power (kW)")
plt.show()

plt.figure()
plt.plot(df["timestamp"], df["power_kw"], label="Original")
plt.plot(df["timestamp"], df["rolling_avg"], label="Rolling Average")
plt.legend()
plt.title("Power Consumption Trend")
plt.xlabel("Time")
plt.ylabel("Power (kW)")
plt.show()


print("\nEnergy Consumption Analysis Completed Successfully ✅")
