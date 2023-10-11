#import dependencies

import os
import csv
#open and read CSV files, skip the header
with open('election_data.csv', newline='') as csv_file :
    election_data = csv.reader(csv_file, delimiter=",")
    election_header = next(csv_file)
    #calculate the total number of votes cast
    voters=[voter[2] for voter in election_data]
    vote_total=len(voters)
    #list of candidates who received the votes using for loop
    candidate_voters=[[voter,voters.count(voter)] for voter in set(voters)]
    #Sort the the variable
    voters_sorted=sorted(voters, key=lambda x:x[1], reverse=True)
    #Calculate the percentage 
    for voter in candidate_voters:
        percentage =(voter[1]/vote_total)*100
        #Print the results
print("----------------------------")
print("Election Results")
print("----------------------------")
print("Total Votes: "+ str(vote_total))
print("------------------------------")
for voter in candidate_voters:
    percentage =(voter[1]/vote_total)*100
    print(f'{voter[0]}:{percentage:6.3f}%({voter[1]})')
print("------------------------------")
#Print winner using the voters sorted becuase the candidates are in a  descending order.
print("Winner: "f'{voters_sorted[0][:]}')

#Export to text file
file = open('output.txt' , 'w')
file.write("----------------------------" + "\n")
file.write("Election Results" + "\n") 
file.write("----------------------------" + "\n")
file.write("Total Votes: "+ str(vote_total) + "\n")
file.write("------------------------------" + "\n")
for voter in candidate_voters:
    percentage =(voter[1]/vote_total)*100
    file.write(f'{voter[0]}:{percentage:6.3f}%({voter[1]})' + "\n")
file.write("------------------------------" + "\n")
file.write("Winner: "f'{voters_sorted[0][:]}' + "\n")
file = open("output.txt", "r")
contents = file.read()
file.close()
print(contents)
