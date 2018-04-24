import csv
with open('test.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

for row in csv.reader(['one,two,three\n','1,2,3']):
    print(row)
