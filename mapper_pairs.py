from mrjob.job import MRJob
from mrjob.step import MRStep
import heapq
import csv

'''
Trying to count the number of internal medicine + cardiology pairs
per state
'''

class build_top_pairs(MRJob):
    def mapper_init(self):
        # We made a big-data-project_storage-bucket and got a 
        # gs link to access the data set through Google 
        gcs_file = gcs.open('gs://big-data-project_storage-bucket/med_data.csv')
        self.data = gcs_file.read()
        gcs_file.close()


    def mapper(self, _, line):
        row1 = line.strip().split(",")
        state1 = row1[10]

        # loop through dataset for every iteration of mapper
        for row in self.data:
            row2 = row.strip().split(",")
            state2 = row2[10]
            if ("Internal Medicine" in row1) and \
                ("Cardiology" in row2) and state1 == state2:
                yield (state1, 1)
    

    def combiner(self, state, counts):
        yield rows, state, sum(counts)


    def reducer(self, state, counts):
        yield state, sum(counts)

 
if __name__ == "__main__":
   build_top_pairs.run()
 