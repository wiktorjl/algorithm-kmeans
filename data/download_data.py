import json
from subprocess import call

def download_data():
    print "Downloading original data set..."
    call(["curl", "--output", "911calls.json",
          "https://data.seattle.gov/api/views/3k2p-39jp/rows.json?accessType=DOWNLOAD"])


def read_raw_data(filename):
    print "Reading original data set..."
    return [[float(x[-7]), float(x[-6])] for x in json.load(open(filename))['data'] if x[-7] is not None and x[-6] is not None]

def store_data(filename, data):
    print "Writing geo coordinates to ", filename, "..."
    with open(filename, "w") as f:
        for element in data:
            f.write(str(element[0]) + " " + str(element[1]) + "\n")


download_data()

store_data("geo.dat", read_raw_data("911calls.json"))
print "Done."