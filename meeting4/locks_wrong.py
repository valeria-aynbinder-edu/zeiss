import threading
import os

total_lines_doubled = 0


folder_path = "/Users/valeria/Downloads/test_data"

total_files = 0

def read_single_file(file_path):
    print(f"Started working on {file_path}")
    global total_lines_doubled
    counter = 0
    with open(file_path, 'r') as f:
        all_lines = f.readlines()
        for l in all_lines:
            total_lines_doubled = total_lines_doubled + 1
            total_lines_doubled = total_lines_doubled + 1
            counter += 1
    print(f"file: {file_path}, counter: {counter}")


all_threads = []

for root, dirs, files in os.walk(folder_path):
    for filename in files:
        if os.path.splitext(filename)[1] == '.csv':
            total_files += 1
            th = threading.Thread(target=read_single_file, args=(os.path.join(root, filename),))
            th.start()
            all_threads.append(th)


for th in all_threads:
    th.join()


print(f"Total files: {total_files}")
print(f"Correct value: {12529*24}")
print(f"Received value: {total_lines_doubled}")