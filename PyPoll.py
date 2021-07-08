# The data we need to retrieve
#Add our dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources","election_results.csv")

#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize total vote counter
total_votes = 0

#Declaring a new list
candidate_options = []

#Declaring a dictionary
candidate_votes ={}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file
with open(file_to_load) as election_data:

    #To do: read and analyze the data here
    file_reader = csv.reader(election_data)

    #Read and print the header row
    headers = next(file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1

        #print the candidate names from each row
        candidate_name = row [2]

        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:

            #add candidate names to the list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        #track candidate's vote count
        candidate_votes[candidate_name] += 1

#Print the total votes.
print(f"The total number of votes casted in Colorado were {total_votes}")

#print the candidate list
print(f"The candidates who contested the election were: {candidate_options}")

#print the candidate vote dictionary
print(f"The votes received by each candidate were: {candidate_votes}")

# Determine the percentage of votes for each candidate by looping through the counts.
#Iterate through the candidate list.
for candidate_name in candidate_votes:

    #Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]

    #Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    #Determine winning vote count and candidate
    #Determine if the votes are greater than winning count
    if(votes > winning_count) and (vote_percentage > winning_percentage):

        #if condition is true
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

        #Print the candidate name and percentage of votes.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based upon popular vote.