import csv
 
reader=csv.reader(open('medicare_data.csv', 'r'), delimiter=',')
writer=csv.writer(open('med_data.csv', 'w'), delimiter=',')
 
entries = set()
 
for row in reader:
   key = (row[0]) # NPI (Physician Identifier)
 
   if key not in entries:
      writer.writerow(row)
      entries.add(key)