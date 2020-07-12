import os
import csv
from statistics import mean
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    #net_total = 0
    row_count = 0
    #changes = {}
    candidates_with_votes = []
    votes = {}
    for row in csvreader:
        row_count += 1
        #net_total += int(row[1])
        if row[2] in candidates_with_votes:
            votes[row[2]] += 1
        else:
            candidates_with_votes.append(row[2])
            votes[row[2]] = 1 
    print(row_count)
    print(candidates_with_votes)
    print(votes)
    print(votes.items())
    sorted_votes = sorted(votes.items(), reverse=True, key=lambda item: item[1])
    print(sorted_votes)
    print(sorted_votes[0][0])
    print(sorted_votes[0][1])
