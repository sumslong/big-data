'''
Analyzing number of providers in states who take Medicare
'''
 
from mrjob.job import MRJob
import re
 
class MRStateAnyTakeMedicare(MRJob):
 
   def mapper(self, _, line):
       COMMA_MATCHER = re.compile(r",(?=(?:[^\"']*[\"'][^\"']*[\"'])*[^\"']*$)")
       line_cols = COMMA_MATCHER.split(line)
       if len(line_cols[10]) == 2 and line_cols[10] != "AA" and line_cols[10] != "ZZ" and line_cols[10] != "XX" and line_cols[10] != "US" and not line_cols[10].isnumeric():
           state = line_cols[10]
       else:
           state = ''
       if state:
           yield (state, 1)
 
   def combiner(self, state, counts):
       yield state, sum(counts)
 
   def reducer(self, state, counts):
       yield state, sum(counts)
 
if __name__ == '__main__':
   MRStateAnyTakeMedicare.run()
