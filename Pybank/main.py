'Importing os module - Allows us to create file paths across operating systems'
import os

'Importing csv module - Allows us to read csv files'
import csv

'Determine csv path - use example python,3,1, Start in resources folder'
budget_csv = os.path.join("..", "Resources", "budget_data.csv")

'open and read csv'
with open(budget_csv) as csv_file:

    'CSV reader specifies delimiter and variable that holds contents'
    csvreader = csv.reader(csv_file, delimiter=",")

    print(csvreader)

    'Reading the header row, exactly like example python-2-08'
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)


'Calculate total months included in the dataset'
'The net total amount of "Profit/Losses" over the entire period'
'Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes'
'The greatest increase in profits (date and amount) over the entire period'
'The greatest decrease in losses (date and amount) over the entire period'



