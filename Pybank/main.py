'Importing os module - Allows us to create file paths across operating systems'
import os

'Importing csv module - Allows us to read csv files'
import csv

'Determine csv path - use example python,3,1, Start in resources folder'
budget_csv = os.path.join( "Resources", "budget_data.csv")

'open and read csv'
with open(budget_csv, newline='') as csv_file:

    'CSV reader specifies delimiter and variable that holds contents'
    csvreader = csv.reader(csv_file, delimiter=",")
    print(csvreader)

    'Reading the header row, exactly like example python-2-08'
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
   
    'set variables'
    total_months = []
    total_profit = []
    change_of_profit = []
    
    print(f"Header: {csv_header}")               
    
    'Calculate total months included in the dataset'
    'Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes'
    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    print(len(total_months))

    for x in range(1, len(total_profit)):
        change_of_profit.append((int(total_profit[x]) - int(total_profit[x-1])))

    'Caluculate greatest increase'
    greatest_increase = max(change_of_profit)

    'Calculate greatest decrease'
    greatest_decrease = min(change_of_profit)


print("Financial Analysis")
print("----------------------------")
print("Total number of months: " + str(len(total_months)))
print("Total: " + "$" + str(sum(total_profit)))
print("Average Change: " + "$" + (str(sum(change_of_profit) / len(change_of_profit))))
print("Greatest Increase in Profits: " + str(total_months[change_of_profit.index(max(change_of_profit))+1]) + " " + "$" + str(greatest_increase))
print("Greatest Decrease in Profits: " + str(total_months[change_of_profit.index(min(change_of_profit))+1]) + " " + "$" + str(greatest_decrease))

file = open("export.txt", "w")
file.write("Financial Analysis" + "\n")
file.write("----------------------------" + "\n")
file.write("Total number of months: " + str(len(total_months)) + "\n")
file.write("Total: " + "$" + str(sum(total_profit)) + "\n")
file.write("Average Change: " + "$" + (str(sum(change_of_profit) / len(change_of_profit))) + "\n")
file.write("Greatest Increase in Profits: " + str(total_months[change_of_profit.index(max(change_of_profit))+1]) + " " + "$" + str(greatest_increase) + "\n")
file.write("Greatest Decrease in Profits: " + str(total_months[change_of_profit.index(min(change_of_profit))+1]) + " " + "$" + str(greatest_decrease) + "\n")


