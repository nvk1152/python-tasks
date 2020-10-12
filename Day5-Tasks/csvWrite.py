import csv

with open('details.csv.','w') as participants:
    writer = csv.writer(participants, delimiter=':')
    writer.writerow(['Name', 'Experinence'])
    writer.writerow(['Vamsi Kishan', '20 years'])
    writer.writerow(['Aishwarya', '10 years'])
    writer.writerow(['Sam', '10 years'])

with open('details.csv.','r') as participants:
    reader = csv.reader(participants, delimiter=':')
    for row in reader:
        print(row, end= ' ')