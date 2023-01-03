
from mrjob.job import MRJob
from mrjob.step import MRStep
import re

class GuestAndStaff(MRJob):
    '''
    Generate a list of provider pairs who can do both internal medicine and cardiology services
    '''

    def mapper(self, _, line):
        row = line.split(",")
        guest = row[0] + row[1]
        staff = row[19] + row[20]

        yield guest, "guest"
        yield staff, "staff"

    def combiner(self, name, people):
        for pers in set(people):
            yield name, pers

    def reducer(self, name, people):
        if len(set(people)) == 2:
            yield name, None


if __name__ == '__main__':
    GuestAndStaff.run()