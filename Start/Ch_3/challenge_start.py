# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data
import datetime
import json
import csv

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD


def getsig(x):
    sig = x["properties"]["sig"]
    return 0 if sig is None else sig


sigevents = sorted(data["features"], key=getsig, reverse=True)
sigevents = sigevents[:40]
# lambda function to get an argument e and return a e["properties"]["time"]
sigevents.sort(key=lambda e: e["properties"]["time"], reverse=True)

header = ["Magnitude", "Place", "Felt Reports", "Date", "gmap link"]
rows = []

for event in sigevents:
    date = datetime.date.fromtimestamp(event["properties"]["time"] / 1000)
    latitude = event["geometry"]["coordinates"][1]
    longitude = event["geometry"]["coordinates"][0]
    gmaplink = f"https://maps.google.com/maps/search/?api=1&query={latitude}%2C{longitude}"

    rows.append([event["properties"]["mag"],
                 event["properties"]["place"],
                 0 if event["properties"]["felt"] is None else event["properties"]["felt"],
                 date,
                 gmaplink])

with open("significantevenets.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(header)
    writer.writerows(rows)
