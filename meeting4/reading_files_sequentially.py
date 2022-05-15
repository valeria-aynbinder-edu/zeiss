import os
import datetime

folder_path = "/Users/valeria/Documents/John Bryce"


def read_single_file(file_path):
    print(f"STARTED working on {os.path.split(file_path)[1]}")
    with open(file_path, 'r') as f:
        all_lines = f.readlines()
        counter = len(all_lines)
    print(f"FINISHED working on {os.path.split(file_path)[1]}: {counter}")


start_time = datetime.datetime.utcnow()

for root, dirs, files in os.walk(folder_path):
    for filename in files:
        if os.path.splitext(filename)[1] == '.csv':
            read_single_file(os.path.join(root, filename))


end_time = datetime.datetime.utcnow()
print(f"total time: {(end_time - start_time).total_seconds()}")


"""
Implement a code that performs the following:
Reads a csv file AAPL.csv and creates separate csv file with stock prices
for every year.
The name of the file should be AAPL_<year>.csv
All the files should be created in parallel

"""