'''
Analyzing number of unique provider types available in an area
'''
 
from mrjob.job import MRJob
import re
 
class MRAreaProviders(MRJob):
 
    def mapper(self, _, line):

        COMMA_MATCHER = re.compile(r",(?=(?:[^\"']*[\"'][^\"']*[\"'])*[^\"']*$)")
        line_cols = COMMA_MATCHER.split(line)

        if len(line_cols) > 13 and "flow" in line_cols[14]:
            area = line_cols[14]
            provider_type = line_cols[16]
        else:
            area = ""
            provider_type = ""

        if area:
            yield (area, provider_type)

 
    def combiner(self, area, provider_type):
        types = set(provider_type)
        for unq_type in types:  
            yield (area, unq_type)


    def reducer(self, area, provider_type):
        types = set(provider_type)
        yield area, len(types)


if __name__ == '__main__':
    MRAreaProviders.run()
