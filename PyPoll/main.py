import os
import csv
from statistics import mean

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    row_count = 0
    candidates_with_votes = []
    votes = {}
    for row in csvreader:
        row_count += 1
        if row[2] in candidates_with_votes:
            votes[row[2]] += 1
        else:
            candidates_with_votes.append(row[2])
            votes[row[2]] = 1 
total_votes = row_count
sorted_votes = sorted(votes.items(), reverse=True, key=lambda item: item[1])

print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(total_votes))
print('-------------------------')
print(sorted_votes[0][0] + ': ' + str(round(100*sorted_votes[0][1]/total_votes,3)) +'% ' + '(' + str(sorted_votes[0][1]) + ')')
print(sorted_votes[1][0] + ': ' + str(round(100*sorted_votes[1][1]/total_votes,3)) +'% ' + '(' + str(sorted_votes[1][1]) + ')')
print(sorted_votes[2][0] + ': ' + str(round(100*sorted_votes[2][1]/total_votes,3)) +'% ' + '(' + str(sorted_votes[2][1]) + ')')
print(sorted_votes[3][0] + ': ' + str(round(100*sorted_votes[3][1]/total_votes,3)) +'% ' + '(' + str(sorted_votes[3][1]) + ')')
print('-------------------------')
print('Winner: ' + sorted_votes[0][0])
print('-------------------------')

first = sorted_votes[0][0]
perc_first = str(round(100*sorted_votes[0][1]/total_votes,3))
votes_first = str(sorted_votes[0][1])

second = sorted_votes[1][0]
perc_sec = str(round(100*sorted_votes[1][1]/total_votes,3))
votes_sec = str(sorted_votes[1][1])

third = sorted_votes[2][0]
perc_third = str(round(100*sorted_votes[2][1]/total_votes,3))
votes_third = str(sorted_votes[2][1])

fourth = sorted_votes[3][0]
perc_fourth = str(round(100*sorted_votes[3][1]/total_votes,3))
votes_fourth = str(sorted_votes[3][1])

output_path = os.path.join('Resources', 'poll_results.csv')
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Total Votes', 'First', 'Percentage', 'Votes', 'Second', 'Percentage', 'Votes', 'Third', 'Percentage', 'Votes', 'Fourth', 'Percentage', 'Votes'])
    csvwriter.writerow([total_votes, first, perc_first, votes_first, second, perc_sec, votes_sec, third, perc_third, votes_third, fourth, perc_fourth, votes_fourth])
