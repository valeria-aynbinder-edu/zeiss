import datetime
import os
from concurrent.futures import ThreadPoolExecutor

PATH = "../meeting3/files/data/AAPL.csv"
OUTPUT_FOLDER = "./output"


def process_file(year):
    print(f"Started working on year {year}")
    lines_to_write = []
    reached_year = False
    with open(PATH, 'r') as f:
        #skip header
        header = f.readline()
        lines_to_write.append(header)

        for line in f:
            cells = line.split(",")
            try:
                date = datetime.datetime.strptime(cells[0], "%d-%m-%Y")
            except:
                print("problem formatting")
                continue

            if date.year == year:
                reached_year = True
                lines_to_write.append(line)
            elif reached_year:
                # all the dates are sorted, we can stop now since
                # we have iterated all the rows of the year
                break
    if len(lines_to_write) > 1:
        filename = os.path.join(OUTPUT_FOLDER, f"aapl_{year}.csv")
        with open(filename, "w") as f:
            f.writelines(lines_to_write)
            print(f"Wrote file {filename}")

if __name__ == '__main__':

    start = datetime.datetime.now()

    with ThreadPoolExecutor(max_workers=10) as executor:
        for year in range(2000, 2021):
            executor.submit(process_file, year)

    end = datetime.datetime.now()
    print(f"Done in {(end-start).total_seconds()}")