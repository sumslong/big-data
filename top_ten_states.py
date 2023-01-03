from mrjob.job import MRJob
import re
import heapq

# Question 5
class MRStateProviders_heap(MRJob):
    '''
    Finds top 10 states for unique types of providers (out of states who take Medicare)
    '''
    def mapper(self, _, line):
        COMMA_MATCHER = re.compile(r",(?=(?:[^\"']*[\"'][^\"']*[\"'])*[^\"']*$)")
        line_cols = COMMA_MATCHER.split(line)
        if len(line_cols[10]) == 2 and line_cols[10] != "AA" and line_cols[10] != "ZZ" and \
        line_cols[10] != "XX" and line_cols[10] != "US" and not line_cols[10].isnumeric():
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
 
    def reducer_init(self):
        self.h = []
 
    def reducer(self, state, provider_type):
        types = set(provider_type)
        num_types = len(types)
        if len(self.h) < 10:
            self.h.append((num_types, state))
            if len(self.h) == 10:
                heapq.heapify(self.h)
        else:
            min_count, _ = self.h[0]
            if num_types > min_count:
                heapq.heapreplace(self.h, (num_types, state))
 
    def reducer_final(self):
        self.h.sort(reverse=True)
        for num_types, state in self.h:
            yield state, num_types
 
if __name__ == '__main__':
  MRStateProviders_heap.run()
