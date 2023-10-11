#import dependencies
import os
import csv
with open ('budget_data.csv', newline='') as csv_file:
    budget_data = csv.reader(csv_file, delimiter=",")
    budget_header = next(csv_file)
    print(f"Header: {budget_header}")
#Total number of months
#The Total ammount of Profit/Losses
    totalmonths = []
    profit_loses = []
    for rows in budget_data:
        profit_loses.append(int(rows[1]))
        totalmonths.append(rows[0])
#The cganges in in Profit/Loses over entire period
profit_loses_change = []
for i in range(1, len(profit_loses)):
    profit_loses_change.append(int(profit_loses[i] - int(profit_loses[i-1])))
#The average change
total_months = len(totalmonths)
profit_loses_average = sum(profit_loses_change) / len(profit_loses_change)
#The greatest increase in profits
greatest_increase = max(profit_loses_change)
#The greatest decrease on profits
greatest_decrease = min(profit_loses_change)
#Print the analysis 
print("Financial Analysis")
print("---------------------------")
print("Total Months: " + str(total_months))
print("Total: " + "$"+ str(sum(profit_loses)))
print("Average Change:"+"$"+str(profit_loses_average))
print("Greatest Increase in profits:" + str(greatest_increase))
print("Greatest Increase in profits:" + str(greatest_decrease))
    #Exporting a text file
file = open("output.txt","w")
file.write("Financial Analysis" + "\n")
file.write("---------------------------" + "\n")
file.write("Total Months:" + str(total_months) + "\n")
file.write("Total:" + "$" + str(sum(profit_loses)) + "\n")
file.write("Average change:"+ "$" + str(profit_loses_average)+ "\n")
file.write("Greatest Increase in Profits: " + str(totalmonths[profit_loses_change.index(max(profit_loses_change))+1]) + "" + "$" + str(greatest_increase) + "\n")
file.write("Greatest Increase in Profits: " + str(totalmonths[profit_loses_change.index(min(profit_loses_change))+1]) + "" + "$" + str(greatest_decrease) + "\n")
file.close()  

file = open("output.txt", "r")
contents = file.read()
file.close()
print(contents)