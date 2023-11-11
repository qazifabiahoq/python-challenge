import csv
import os

csv_path = os.path.join(os.path.dirname(__file__), "Resources", "election_data.csv")

#  These are the Variables to keep track of the greatest increase and decrease
total_votes = 0
candidates = []
votes_received = {}

with open(csv_path, 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip the header row

    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        if candidate not in candidates:
            candidates.append(candidate)
            votes_received[candidate] = 0
        
        votes_received[candidate] += 1

# This is the winner and calculating vote percentages
winner = ""
winning_votes = 0
results = []

for candidate, votes in votes_received.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
    
    if votes > winning_votes:
        winning_votes = votes
        winner = candidate


print("Election Results")
print("-" * 25)
print(f"Total Votes: {total_votes}")
print("-" * 25)
for result in results:
    print(result)
print("-" * 25)
print(f"Winner: {winner}")
print("-" * 25)

# Define the output file path
output_file_path = os.path.join(os.path.dirname(__file__), "Analysis", "election_results.txt")


with open(output_file_path, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-" * 25 + "\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-" * 25 + "\n")
    for result in results:
        output_file.write(result + "\n")
    output_file.write("-" * 25 + "\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-" * 25 + "\n")



