from mrjob.job import MRJob
import re
import heapq
 
# Question 1
class MRAreaProviders_Heap(MRJob):
    '''
    Finds top 10 areas for number of unique provider types available
    '''
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
 
    def reducer_init(self):
        self.h = []
 
    def reducer(self, area, provider_type):
        types = set(provider_type)
        num_types = len(types)
        if len(self.h) < 10:
            self.h.append((num_types, area))
            if len(self.h) == 10:
                heapq.heapify(self.h)
        else:
            min_count, _ = self.h[0]
            if num_types > min_count:
                heapq.heapreplace(self.h, (num_types, area))
 
    def reducer_final(self):
        self.h.sort(reverse=True)
        for num_types, area in self.h:
            yield area, num_types
 
if __name__ == '__main__':
    MRAreaProviders_Heap.run()
