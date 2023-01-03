'''
Analyzing diversity of services in states who take Medicare
'''
 
from mrjob.job import MRJob
import re
 
class MRStateProviders(MRJob):
 
   def mapper(self, _, line):
       COMMA_MATCHER = re.compile(r",(?=(?:[^\"']*[\"'][^\"']*[\"'])*[^\"']*$)")
       line_cols = COMMA_MATCHER.split(line)
       if len(line_cols[10]) == 2 and line_cols[10] != "AA" and line_cols[10] != "ZZ" and line_cols[10] != "XX" and line_cols[10] != "US" and not line_cols[10].isnumeric():
           state = line_cols[10]
           provider_type = line_cols[16]
       else:
           state = ""
           provider_type = ""
       if state:
           yield (state, provider_type)
 
   def combiner(self, state, provider_type):
       types = set(provider_type)
       for unq_type in types:  
           yield (state, unq_type)
      
   def reducer(self, state, provider_type):
       types = set(provider_type)
       yield state, len(types)
 
if __name__ == '__main__':
   MRStateProviders.run()
