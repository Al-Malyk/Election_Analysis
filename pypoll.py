import csv
import os
# create a file to load file to path
file_to_load = os.path.join('Resourses', 'election_results.csv')
# create a variable to save file to path
file_to_save = os.path.join("analysis" , "election_analysis.txt")
     # seems like outfile is the file object. its used to refer to the created txt file
with open(file_to_save , 'w') as text_file:
      text_file.write('Counties in the Election\n')
      text_file.write('-' * 15)
      text_file.write('\n')
      text_file.write('Arapahoe\nDenver\nJefferson')

# code block in line 8 was practice. MIGHT DELETE
with open(file_to_load) as election_data:
     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)
     headers = next(file_reader)
     print(headers)
