from collections import defaultdict, Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for s in strs:
            freq = Counter(s)
            code = "".join(
                [alpha + str(freq[alpha]) for alpha in sorted(freq.keys())]
            )
            ana[code].append(s)
        return list(ana.values())
