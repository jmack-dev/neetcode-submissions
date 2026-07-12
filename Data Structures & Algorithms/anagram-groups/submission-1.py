class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: List[List[str]] = []

        for s in strs:
            duplicate: bool = False

            for grp in anagrams:
                if Solution._isAnagram(s, grp[0]):
                    grp.append(s)
                    duplicate = True
                    break
            
            if not duplicate:
                anagrams.append([s])

        return anagrams


    def _isAnagram(s: str, t: str) -> bool:
        # copied from previous problem
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