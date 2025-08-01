import csv

# 1.
with open('path/to/csv_file', 'r') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        print(line)

# 2.
with open('country.csv', encoding="utf8") as f:
    csv_reader = csv_reader(f)
    for line in csv_reader:
        print(line)

# 3. 
with open('country.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)
    for line_no, line in enumerate(csv_reader, 1):
        if line_no == 1:
            print('Header:')
            print(line)  # header
            print('Data:')
        else:
            print(line)  # data

# 4.
total_area = 0
# calculate the total area of all countries
with open('country.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)

    # skip the header
    next(csv_reader)

    # calculate total
    for line in csv_reader:
        total_area += float(line[1])

print(total_area)