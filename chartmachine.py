import sys
import json
class cm:
    def __init__(self, algo_type, jobs):
        self.algo_type = algo_type
        self.parsed_jobs = self.parse_jobs(jobs)
        pass
    def parse_jobs(self,jstring):
        jstring = jstring.replace("x",",")
        print(jstring)

        pass
    def print_chart(self):
        pass

algo_type = sys.argv[1]
jobs = sys.argv[2]
#job [[0x1],[1x1]]

print(algo_type)
print(jobs)
chartmachinator = cm(algo_type, jobs)