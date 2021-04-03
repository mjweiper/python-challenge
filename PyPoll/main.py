'Importing os module - Allows us to create file paths across operating systems'
import os

'Importing csv module - Allows us to read csv files'
import csv

'Determine csv path - use example python,3,1, Start in resources folder'
election_csv = os.path.join( "Resources", "election_data.csv") 

'open and read csv'
with open(election_csv, newline='') as csv_file:

    'CSV reader specifies delimiter and variable that holds contents'
    csvreader = csv.reader(csv_file, delimiter=",")
    print(csvreader)

    'Reading the header row, exactly like example python-2-08'
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    'set variables'
    votes = 0
    candidates = []
    votes_candidate = []
    percent_votes = []
    max_votes = votes_candidate[0]
    max_index = 0

    print(f"Header: {csv_header}") 

    for row in csvreader:
        
        'Count votes'
        votes += 1

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            votes_candidate.append(1)

        else:
            index = candidates.index(row[2])
            votes_candidate[index] += 1


    for x in votes_candidate:

        percentage = (x/votes_candidate) * 100
        percent_votes.append(percentage)


    winner = max(votes_candidate)
    index = votes_candidate.index(winner)
    value_winner = candidates[index]

print("Election Results")
print("-------------------------")
print("Total Votes: " +  str(sum(votes_candidate)))
print("-------------------------")
for y in range(len(candidates)):
    print(f"{candidates[y]}: {str(percent_votes[y])} ({str(votes_candidate[y])})")
print("-------------------------")
print(f"Winner: {value_winner}")
print("-------------------------")

file = open("export.txt", "w")
file.write("Election Results" + "\n")
file.write("----------------------------" + "\n")
file.write("Total Votes: " +  str(sum(votes_candidate)) + "\n")
file.write("----------------------------" + "\n")
file.write(f"{candidates[y]}: {str(percent_votes[y])} ({str(votes_candidate[y])})" + "\n")
file.write("----------------------------" + "\n")
file.write(f"Winner: {value_winner}" + "\n")
file.write("----------------------------" + "\n")

    


    

