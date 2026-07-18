class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        starts = []
        for v in nums:
            if v-1 not in seen:
                starts.append(v)
        
        max_count = 0
        for s in starts:
            count = 1
            while True:
                if s+count not in seen:
                    break
                count += 1
                

            if count > max_count:
                max_count = count

        return max_count