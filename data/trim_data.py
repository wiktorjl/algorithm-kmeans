def read_data(filename):
    with open(filename) as f:
        return [tuple(line.strip().split(" ")) for line in f.readlines()]

def write_data(data, filename):
    with open(filename, "w") as f:
        f.writelines(data)

data = read_data("geo.dat")
data = [str(item[0]) + " " + str(item[1]) + "\n" for item in data[:5000]]
write_data(data, "geo_trimmed.dat")
