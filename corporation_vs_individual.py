'''
Analyzing number of corporations vs. individuals who take Medicare
'''
 
from mrjob.job import MRJob
import re
 
class MRCorpAndIndividual(MRJob):
 
   def mapper(self, _, line):
       COMMA_MATCHER = re.compile(r",(?=(?:[^\"']*[\"'][^\"']*[\"'])*[^\"']*$)")
       line_cols = COMMA_MATCHER.split(line)
       individual = line_cols[5]
       if individual == "F" or individual == "M":
           yield ("individual", 1)
       else:
           yield ("corporation", 1)
 
   def combiner(self, type, counts):
       yield type, sum(counts)
 
   def reducer(self, type, counts):
       yield type, sum(counts)
 
if __name__ == '__main__':
   MRCorpAndIndividual.run()
