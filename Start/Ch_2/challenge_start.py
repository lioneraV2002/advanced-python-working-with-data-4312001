# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import collections

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# use a default dictionary to categorize each event and count each one
totals = collections.defaultdict(int)
for event in data["features"]:
    totals[event["properties"]["type"]] += 1

for k, v in totals.items():
    # 15 means to specify the length of the f-string field that k will occupy
    # if the length is less than 15, then spaces will be added to make up for the difference
    # if not, the width of the field will automatically expand

    print(f"{k:15}: {v}")
