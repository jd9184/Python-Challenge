import csv
from distutils import text_file

file_to_load = "Resources/election_data.csv"
file_to_output = "Analysis/election_analysis.txt"

#Total Votes
total_votes = 0

# candidate and vote counters
candidate_options = []
candidate_votes = {}

#winning candidate and winning count
winning_candidate = ""
winning_count = 0

#read the csv and convert to dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    next(reader)

    #for each row
    for row in reader:
        
        #print(row)

      #add to the total vote count
        total_votes = total_votes + 1

        #extrct candidate name for each row
        candidate_name = row[2]
        #print(candidate_name)

        #if the candidate does not match any existing candidate
        if candidate_name not in candidate_options:

            #add it to the list of candidates in the running
            candidate_options.append(candidate_name)

            #begin tracking that candidates voter count
            candidate_votes[candidate_name] = 0

        #Then add a vote to that candidates count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

    #print the final vote count
    # elect_results = (
    #     f"\n\Election Results\n"
    #     f"--------------------------\n"
    #     f"total Votes: {total_votes}\n"
    #     f"--------------------------\n"
    # )

#print(elect_results)

# Print the results and export the data to our text file
with open(file_to_output, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

# determine the winner by looping through the counts
    for candidate in candidate_votes:

        #retrieve the winner by looping through the counts
        votes = candidate_votes.get(candidate)
        votes_percentage = float(votes) / float(total_votes) * 100

        #print each candidates voter count and percentage
        voter_output = f"{candidate}: {votes_percentage: .3f}% ({votes})\n"

        print(voter_output) 

        txt_file.write(voter_output)


# determine winning vote count and candidate
 
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate


    # print the winning candidate
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"--------------------------\n"
    )

    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)