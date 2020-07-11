import os
import csv
from statistics import mean
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    net_total = 0
    row_count = 0
    changes = {}
    for row in csvreader:
        row_count += 1
        net_total += int(row[1])
        #print(row)
        if row_count != 1:
            change = int(row[1]) - last_month
            changes[row[0]] = change
        last_month = int(row[1])
    maxi = max(changes.values())
    for item in changes.items():
        if item[1] == maxi:
            month = item[0]
    print(row_count)
    print(net_total)
    print(mean(changes.values()))
    print(maxi)
    print(month)
    print(min(changes.values()))
