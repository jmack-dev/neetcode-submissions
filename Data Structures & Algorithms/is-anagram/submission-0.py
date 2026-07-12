class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs = {}

        for c in s:
            if c not in freqs:
                freqs[c] = 1
            else:
                freqs[c] += 1
            
        for c in t:
            if c not in freqs:
                return False
            
            freqs[c] -= 1
        
        for v in freqs.values():
            if v != 0:
                return False

        return True
            