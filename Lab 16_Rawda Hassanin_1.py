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
        
        
#Graphing the data
plt.style.use('seaborn-v0_8-bright')
figure, graph = plt.subplots()

graph.set_title("Ohio Unemployment(by Months) 1976-2022 ", fontsize=20,color='blue', pad=20)
graph.set_xlabel("Date", fontsize=16, color='black', labelpad=15)
graph.set_ylabel("Unemployment Rate (%)",fontsize=16, color='black', labelpad=15)
figure.autofmt_xdate()

graph.plot(Dates,Rates, c='red')
plt.show()        
