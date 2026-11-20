from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs = Counter(s)
        freqt = Counter(t)
        return freqs == freqt