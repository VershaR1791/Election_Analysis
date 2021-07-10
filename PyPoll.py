#Adding dependencies
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

#Save the results to our text file.
with open(file_to_save,"w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")
    print(election_results, end="")

    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
