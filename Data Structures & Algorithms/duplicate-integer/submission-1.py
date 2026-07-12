class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for elm in nums:
            retrieved = seen.get(elm, -1)

            if retrieved >= 0:
                return True
            seen[elm] = 1
        return False