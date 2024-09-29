# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyPoll/Resources/election_data.csv")  # Input file path
file_to_output = os.path.join("PyPoll/Resources/election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
List_candidates = []  # Track the complete list of candidates who received votes
candidate_votes = {}  # Dictionary to track votes for each candidate

# Open the CSV file and process it
with open(file_to_load) as election_data:
    Votes_reader = csv.reader(election_data)

    # Skip the header row
    header = next(Votes_reader)

    # Loop through each row of the dataset and process it
    for row in Votes_reader:
        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]  # Assuming candidate name is in the third column

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in List_candidates:
            List_candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0  # Initialize candidate's vote count

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("----------------------------\n")
    # Print the total vote count (to terminal)
    print(f"Total Votes: {total_votes}")
    # Write the total vote count to the text file
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("----------------------------\n")

    # Initialize variables to track the winning candidate
    winning_candidate = ""
    winning_count = 0

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in List_candidates:
        # Get the vote count and calculate the percentage
        votes = candidate_votes[candidate]
        percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        print(f"{candidate}: {percentage:.3f}% ({votes})")
        txt_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    # Generate and print the winning candidate summary
    print("-------------------------")
    print(f"Winner: {winning_candidate}")
    print("-------------------------")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winning_candidate}\n")
    txt_file.write("-------------------------\n")