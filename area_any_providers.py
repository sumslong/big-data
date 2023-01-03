'''
Analyzing the quantity of providers available in an area
'''

from mrjob.job import MRJob
import re
 
class MRAreaAnyProviders(MRJob):
 
   def mapper(self, _, line):
      COMMA_MATCHER = re.compile(r",(?=(?:[^\"']*[\"'][^\"']*[\"'])*[^\"']*$)")
      line_cols = COMMA_MATCHER.split(line)
    
      if len(line_cols) > 13 and "flow" in line_cols[14]:
          area = line_cols[14]
      else:
          area = ""
      if area:
          yield (area, 1)
 
   def combiner(self, area, counts):
       yield area, sum(counts)
 
   def reducer(self, area, counts):
       yield area, sum(counts)
 
if __name__ == '__main__':
   MRAreaAnyProviders.run()
