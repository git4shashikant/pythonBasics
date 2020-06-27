import csv

# reading row by row
with open('../files/csv_test.csv', 'rt') as f:
    data = csv.reader(f)
    for row in data:
        print(row)


# reading as dictionary
reader = csv.DictReader(open('../files/csv_test.csv'))
for row in reader:
    print(row)


with open('../files/csv_test_1.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['9', '10', '11', '12'])


