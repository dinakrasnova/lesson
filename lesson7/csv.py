import csv
# csv.writer
car_data = [['mark', 'fuel_rate', 'amount'],['Volvo', 15.2, 2500000.0]]

with open('example.csv', 'w') as f:
    writer = csv.writer(f, delimiter = '&') #
    writer.writerows(car_data)
print('Writing complete!')

# csv.reader

with open('example.csv') as f:
    reader = csv.reader(f,delimiter = '&')
    for row in reader:
        print(row)