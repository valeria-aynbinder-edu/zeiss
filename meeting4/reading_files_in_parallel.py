import os
import threading
import datetime


folder_path = "/Users/valeria/Documents/John Bryce"


def read_single_file(file_path):
    print(f"STARTED working on {os.path.split(file_path)[1]}")
    with open(file_path, 'r') as f:
        all_lines = f.readlines()
        counter = len(all_lines)
    print(f"FINISHED working on {os.path.split(file_path)[1]}: {counter}")


start_time = datetime.datetime.utcnow()

all_threads = []

for root, dirs, files in os.walk(folder_path):
    for filename in files:
        if os.path.splitext(filename)[1] == '.csv':
            th = threading.Thread(target=read_single_file, args=(os.path.join(root, filename),))
            th.start()
            all_threads.append(th)


for th in all_threads:
    th.join()


end_time = datetime.datetime.utcnow()
print(f"total time: {(end_time - start_time).total_seconds()}")