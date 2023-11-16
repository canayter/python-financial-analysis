#!/usr/bin/env python
# coding: utf-8

# In[11]:


#importing modules
import csv
import os

#defining file paths for files going to be used to load and output
file_to_load = os.path.join(".", "Resources", "election_data.csv")
file_to_output = os.path.join(".", "election_analysis.txt")

#defining a total vote counter
total_votes = 0

#creating candidate options and vote counters
candidate_votes = {}
candidate_options = []

#creating winning candidate and winning count trackers
winning_candidate = ""
winning_count = 0

with open(file_to_load) as election_data:
    
#reading the headers
    reader = csv.reader(election_data)
    header = next(reader)
    
    for row in reader:
        
#calculating by adding to the total vote count
        total_votes = total_votes + 1

#getting the candidate name from each row
        candidate_name = row[2]
    
#defining a condition to loop through candidates and adds candidates to the list
        if candidate_name not in candidate_options:
        
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
            
        candidate_votes[candidate_name] += 1

with open(file_to_output, "w") as txt_file:
#showing the total number of votes cast
    output = (
        f"Election Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"--------------------------\n")
    print(output)
    
    txt_file.write(output)

#showing the complete list of candidates who received any votes
    
    for candidate in candidate_votes:
        
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        
        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
            
#calculating the percentage of votes each candidate won andt he total number of votes each candidate won
        
        voter_output = f"{candidate}: {vote_percentage}% ({votes})\n"
        
        print(voter_output)
        
        txt_file.write(voter_output)
        
#calculating the winner of the election based on popular vote
    
    winning_candidate = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"--------------------------\n")
    print(winning_candidate)
    
    txt_file.write(winning_candidate)


# In[ ]:




