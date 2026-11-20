from collections import defaultdict, Counter
from string import ascii_lowercase


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for s in strs:
            freq = Counter(s)
            code = "".join([alpha + str(freq[alpha]) for alpha in ascii_lowercase if alpha in freq])
            ana[code].append(s)
        return list(ana.values())
