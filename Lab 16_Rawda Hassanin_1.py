"""
Lab 16: Ohio Unemployment Rate Analysis and Visualization

Lab 16_Rawda Hassanin_1.py
Name: Rawda Hassanin
Date: 2024-06-15
Description:
This program reads unemployment data from the 'OHUR.csv' file downloaded from 
the FRED Economic Data site. It performs the following tasks:

1. Reads and parses the CSV file.
2. Analyzes the header using the enumerate() function.
3. Converts the 'DATE' column into datetime objects for accurate plotting.
4. Extracts unemployment rates as float values, handling missing or invalid data.
5. Plots the unemployment rate over time with labeled axes.

Inputs:
- 'OHUR.csv' file containing monthly national unemployment rates.
Outputs:
- A line graph of the unemployment rate over time with properly formatted x-axis dates.
"""

from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Read CSV file and split into lines
path = Path('OHUR.csv')
lines = path.read_text(encoding="utf-8").splitlines()

# Parse CSV reader and header
reader = csv.reader(lines)
header_row = next(reader)

# Analyze header using enumerate() to display column indices
for index, col_title in enumerate(header_row):
      print(f"{index}: {col_title}",  end=' ') 
print()

# Lists to store parsed dates and unemployment rates
Dates = []
Rates = []

# Parse each row for date and rate
for row in reader:
    # Handle missing or invalid data
    try:
        # Convert string to datetime object
        current_date = datetime.strptime(row[0], "%Y-%m-%d") 
        
        Rate = float(row[1]) # Convert rate to float
    except ValueError:
        print(f"Missing data for {Rate}")
    else:
        Dates.append(current_date)
        Rates.append(Rate)
        
        
#Graphing the data

plt.style.use('seaborn-v0_8-bright')
figure, graph = plt.subplots()

graph.set_title("Ohio Unemployment(by Months) 1976-2022 ", fontsize=20,color='blue', pad=20)
graph.set_xlabel("Date", fontsize=16, color='black', labelpad=15)
graph.set_ylabel("Unemployment Rate (%)",fontsize=16, color='black', labelpad=15)
figure.autofmt_xdate()  # Auto-format date labels for readability

# Plot the data
graph.plot(Dates,Rates, c='red')

plt.show()        
