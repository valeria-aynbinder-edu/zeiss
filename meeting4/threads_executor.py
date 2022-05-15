from concurrent.futures import ThreadPoolExecutor
import os

folder_path = "/Users/valeria/Downloads/test_data"
# folder_path = "/Users/valeria/Documents/John Bryce"
total_lines = 0


def read_single_file(file_path):
    print(f"STARTED working on {os.path.split(file_path)[1]}")
    with open(file_path, 'r') as f:
        all_lines = f.readlines()
        counter = len(all_lines)
    print(f"FINISHED working on {os.path.split(file_path)[1]}: {counter}")
    return counter


futures = []

with ThreadPoolExecutor(max_workers=4) as executor:
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if os.path.splitext(filename)[1] == '.csv':
                future = executor.submit(read_single_file, os.path.join(root, filename))
                futures.append(future)

print("after executor")

for future in futures:
    return_value = future.result()
    total_lines += return_value
    print(return_value)

print(f"Total lines: {total_lines}")