import csv
import os

file_path = "./Resources/election_data.csv"

if os.path.exists(file_path):
    # Initialize candidate_votes dictionary to store the count of votes for each candidate
    candidate_votes = {}

    # Opening and reading data from csv file
    with open(file_path, newline='') as election_data:
        reader = csv.reader(election_data)

        header = next(reader)  # Skip the header row

        for row_num, row in enumerate(reader, start=2):  # Start counting from the second row since we skipped the header
            try:
                candidate = row[2]  #candidate's name is in the third column (index 2)
                # Update candidate_votes dictionary
                if candidate in candidate_votes:
                    candidate_votes[candidate] += 1
                else:
                    candidate_votes[candidate] = 1
            except IndexError:
                print(f"Error: Row {row_num} has fewer columns than expected.")
                continue

    # Calculate total number of votes cast
    total_votes = sum(candidate_votes.values())

    # Find the winning candidate
    winning_candidate = max(candidate_votes, key=candidate_votes.get)
    winning_votes = candidate_votes[winning_candidate]

    # Print results
    print("Total number of votes cast:", total_votes)
    print("List of candidates and their percentage of votes:")
    for candidate, votes in candidate_votes.items():
        percent = (votes / total_votes) * 100
        print(f"{candidate}: {percent:.2f}% ({votes})")
    print("Winning candidate:", winning_candidate, "with", winning_votes, "votes")

 # Create the 'Analysis' folder if it doesn't exist
    if not os.path.exists('Analysis'):
        os.makedirs('Analysis')

    # Path for the output text file within the 'Analysis' folder
    output_file_path = os.path.join('Analysis', 'analysis_result.txt')

    # Write analysis results to a text file
    with open(output_file_path, 'w') as file:
        file.write("Total number of votes cast: {}\n".format(total_votes))
        file.write("List of candidates and their percentage of votes:\n")
        for candidate, votes in candidate_votes.items():
            percent = (votes / total_votes) * 100
            file.write(f"{candidate}: {percent:.2f}% ({votes})\n")
        file.write("Winning candidate: {} with {} votes\n".format(winning_candidate, winning_votes))

    print("Analysis results have been written to", output_file_path)

else:
    print("Error: File not found or invalid file path.")