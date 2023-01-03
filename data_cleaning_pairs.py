import csv
import re
 
# filename = 'med_data.csv'
# writer=csv.writer(open('med_data_paired.csv', 'w'), delimiter=',')

# with open(filename, 'r') as csvfile:
#     datareader = csv.reader(csvfile)
#     for row1 in datareader:
#         for row2 in datareader:
#             if ("Internal Medicine" in row1) and ("Cardiology" in row2):
#                 writer.writerow(row1 + row2)


reader=csv.reader(open('med_data.csv', 'r'), delimiter=',')
writer=csv.writer(open('med_data_paired.csv', 'w'), delimiter=',')
 
for row1 in reader:
    row1_string = ",".join(row1)
    COMMA_MATCHER1 = re.compile(r",(?=(?:[^\"']*[\"'][^\"']*[\"'])*[^\"']*$)")
    line1 = COMMA_MATCHER1.split(row1_string)
    state1 = line1[10]
    for row2 in reader:
        row2_string = ",".join(row2)
        COMMA_MATCHER2 = re.compile(r",(?=(?:[^\"']*[\"'][^\"']*[\"'])*[^\"']*$)")
        line2 = COMMA_MATCHER2.split(row2_string)
        if len(line2) > 11:
            state2 = line2[10]
        else:
            state2 = "None"
        
        if ("Internal Medicine" in row1) and ("Cardiology" in row2) and state1 == state2:
            writer.writerow(row2)