import csv

d1 = []
d2 = []

with open('bright_stars.csv') as f:
    reader = csv.reader(f)

    for i in reader:
        d1.append(i)

with open('dwarf_proccessed.csv') as f:
    reader = csv.reader(f)

    for i in reader:
        d2.append(i)

h = d1[0]

t1 = d1[1:]
t2 = d2[1:]

data = []

for i in t1:
    data.append(i)

for i in t2:
    data.append(i)

with open('merged.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(h)
    writer.writerows(data)

