# Example file for Advanced Python: Working With Data by Joe Marini
# read data from a CSV file into an object structure

import csv
import pprint

# read the contents of a CSV file into an object structure
result = []

# TODO: open the CSV file for reading
with open("largequakes.csv", "r") as csvfile:
    # create the reader object to read the file
    reader = csv.reader(csvfile)

    # does the file contain headers?

    # This creates an instance of the Sniffer class,
    # which is used to detect the format of a CSV file.
    sniffer = csv.Sniffer()

    # These lines read the first 1024 bytes of the CSV file and
    # reset the file pointer to the beginning of the file.
    # This is necessary because the Sniffer class needs to examine a sample of the file
    # in order to determine its format.
    sample = csvfile.read(1024)
    csvfile.seek(0)

    # check whether the sample has a header or not
    if sniffer.has_header(sample):
        next(reader)

    # iterate over each row
    for row in reader:
        print(row)

        #   add date to our list

        result.append({
            "place": row[0],
            "magnitude": row[1],
            "date": row[2],
            "link": row[3],
        })

pprint.pp(result)
