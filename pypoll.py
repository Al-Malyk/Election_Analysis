# Import dependencies 
import csv
import os

#Bind file paths to variables
file_to_load = os.path.join("Resourses" , "election_results.csv")
file_to_save = os.path.join("analysis" , "election_analysis.txt")

#Define vote counter 
total_votes = 0
# list and dict for candidates
candidate_options = []
candidate_votes = {}
# Winner stat variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the csv file and read it, ignoring setting a mode opens in read by default i think
with open(file_to_load) as election_data:
     file_reader = csv.reader(election_data)

     #(Read the header row) not sure
     headers = next(file_reader)
     #loop through rows find candidates and votes 
     for row in file_reader:
          total_votes += 1
          candidate_name = row[2]
          
          if candidate_name not in candidate_options:
               candidate_options.append(candidate_name)
               # track each candidates votes
               candidate_votes[candidate_name] = 0
          #increment candidate vote
          candidate_votes[candidate_name] += 1

# save this in our write file
with open(file_to_save, 'w') as txt_file:
     election_results = (
          f"\nElection Results\n"
          f"-------------------------\n"
          f"Total Votes: {total_votes:,}\n"
          f"-------------------------\n")
     print(election_results, end="")
     txt_file.write(election_results)
          #find vote percentage and determine winner
     for candidate_name in candidate_votes:
          votes = candidate_votes[candidate_name]
          #find vote percentage
          vote_percentage = float(votes)/float(total_votes) * 100
          # Print each candidate, their voter count, and percentage to the
          # terminal.
          candidate_results = f"{candidate_name}:  {vote_percentage:.1f}% ({votes:,} votes)\n"
          txt_file.write(candidate_results)
          print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
          # find winner
          if votes > winning_count and vote_percentage > winning_percentage:
               winning_count = votes
               winning_percentage = vote_percentage
               winning_candidate = candidate_name
     # Print the winning candidates' results to the terminal.
     winning_candidate_summary = (
          f'---------------\n'
          f'Winner: {winning_candidate}\n'
          f'Winning Votes: {winning_count:,}\n'
          f'Winning Percentage: {winning_percentage:.1f}%\n'
          f'----------------')
     txt_file.write(winning_candidate_summary)
     # Print the final vote count to the terminal.
     
     # Save the final vote count to the text file.
     
     
     
          




