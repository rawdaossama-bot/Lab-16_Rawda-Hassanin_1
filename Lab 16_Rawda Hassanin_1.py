from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('OHUR.csv')
lines = path.read_text(encoding="utf-8").splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, col_title in enumerate(header_row):
      print(f"{index}: {col_title}",  end=' ') 
print()

  
Dates = []
Rates = []

for row in reader:
    try:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        
        Rate = float(row[1])
    except ValueError:
        print(f"Missing data for {Rate}")
    else:
        Dates.append(current_date)
        Rates.append(Rate)
        
