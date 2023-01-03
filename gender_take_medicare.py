'''
Analyzing proportion of men/women who take Medicare
'''
 
from mrjob.job import MRJob
import re
 
class MRGenderTakeMedicare(MRJob):
 
   def mapper(self, _, line):
       COMMA_MATCHER = re.compile(r",(?=(?:[^\"']*[\"'][^\"']*[\"'])*[^\"']*$)")
       line_cols = COMMA_MATCHER.split(line)
       gender = line_cols[5]
       if gender == "M" or gender == "F":
           yield (gender, 1)
 
   def combiner(self, gender, counts):
       yield gender, sum(counts)
 
   def reducer(self, gender, counts):
       yield gender, sum(counts)
 
if __name__ == '__main__':
   MRGenderTakeMedicare.run()
