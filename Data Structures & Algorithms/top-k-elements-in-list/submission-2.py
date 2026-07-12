from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        k_max = 10**4 + 1
        k_idx = 0
        groups = [[] for _ in range(len(nums) + 1)]

        for v, c in counter.items():
            groups[c].append(v)
        print(counter)
        print(groups)

        result = []
        found = 0
        for group in groups[::-1]:
            if found == k:
                break

            if group:
                for v in group:
                    result.append(v)
                    found += 1

        return result

        