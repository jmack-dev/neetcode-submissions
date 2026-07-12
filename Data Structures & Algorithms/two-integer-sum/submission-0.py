class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairings: Dict[int, int] = {}

        for i, n in enumerate(nums):
            if n in pairings:
                return [pairings[n], i]

            pairings[target - n] = i