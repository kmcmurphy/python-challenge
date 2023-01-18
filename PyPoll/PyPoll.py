import os
import csv
import numpy as np

#NEED TO INVESTIGATE - BE SURE YOU'RE IN THE RIGHT TERMINAL DIRECTORY TO RUN
csvpath = os.path.join('Resources','election_data.csv')

# Set variables to contain data
data = []
candidates = []
total_votes = 0
charles_votes = 0
diane_votes = 0
raymon_votes = 0

with open(csvpath, encoding="utf8") as csvfile:

        csvreader = csv.reader(csvfile, delimiter=',')

        # Skip the file header
        csvheader = next(csvreader)
        
        for row in csvreader:

            data.append(row[0])

            #Determine names of canidates
            candidates.append(row[2])

            if (row[2] == "Charles Casper Stockham"):
                charles_votes +=1

            if (row[2] == "Diana DeGette"):
                diane_votes += 1

            if (row[2] == "Raymon Anthony Doane"):
                raymon_votes += 1

        # Get the total number of votes
        total_votes = len(data)

        # Get unique candidate list for logic above
        #print(np.unique(candidates))

        # Calculate the precentage of the vote for each candidate
        charles_percent = (charles_votes/total_votes)*100
        diane_percent = (diane_votes/total_votes)*100
        raymon_percent = (raymon_votes/total_votes)*100
        

        #Determine which candidate has the most votes
        if charles_votes > diane_votes and charles_votes > raymon_votes:
            winner = "Charles Casper Stockham"

        elif diane_votes > charles_votes and diane_votes > raymon_votes:
            winner = "Diana DeGette"

        else:
            winner = "Raymon Anthony Doane"

        #Prepare data for output
        output_lines = [
        "Election Results",
        "-------------------------",
        f"Total Votes: {total_votes}",
        "-------------------------",
        f"Charles Casper Stockham: {round(charles_percent,3)}% ({charles_votes})",
        f"Diana DeGette: {round(diane_percent,3)}% ({diane_votes})",
        f"Raymon Anthony Doane: {round(raymon_percent,3)}% ({raymon_votes})",
        "-------------------------",
        f"Winner: {winner}",
        "-------------------------"]

# Specify the file to write to
output_path = os.path.join("Output", "new.txt")

# Open a file using "write" mode and create a variable to hold output
with open(output_path, 'w') as txtfile:

    # Take each line/item from list and add a line break
    txtfile.write('\n'.join(output_lines))

    
