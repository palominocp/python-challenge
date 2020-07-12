import os
import csv
from statistics import mean
import locale

locale.setlocale( locale.LC_ALL, '' )

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    net_total = 0
    row_count = 0
    changes = {}
    for row in csvreader:
        row_count += 1
        net_total += int(row[1])
        if row_count != 1:
            change = int(row[1]) - last_month
            changes[row[0]] = change
        last_month = int(row[1])

great_inc = max(changes.values())
great_dec = min(changes.values())
for item in changes.items():
    if item[1] == great_inc:
        month_inc = item[0]
    if item[1] == great_dec:
        month_dec = item[0]
number_of_months = row_count
net_total_formatted = locale.currency(net_total)
avg_of_changes = locale.currency(mean(changes.values()))
greatest_increase = locale.currency(great_inc)
greatest_decrease = locale.currency(great_dec)
print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(number_of_months))
print('Total: ' + net_total_formatted)
print('Average  Change: ' + avg_of_changes)
print('Greatest Increase in Profits: ' + month_inc + ' (' + greatest_increase +')')
print('Greatest Decrease in Profits: ' + month_dec + ' (' + greatest_decrease +')')
    
output_path = os.path.join('Resources', 'results.csv')
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Number of months', 'Net Profit/Losses', 'Avg of Changes', 'Greatest Increase', 'Month', 'Greatest Decrease', 'Month'])
    csvwriter.writerow([number_of_months, net_total_formatted, avg_of_changes, greatest_increase, month_inc, greatest_decrease, month_dec])
