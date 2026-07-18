class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        ordered = list(sorted(nums))

        for i in range(len(ordered)-2):
            start = i+1
            end = len(ordered) - 1
            target = ordered[i] * -1

            while start < end:
                if ordered[start] + ordered[end] == target:
                    result.add((ordered[i], ordered[start], ordered[end]))
                if ordered[start] + ordered[end] > target:
                    end -= 1
                else:
                    start += 1

        return [list(l) for l in result]