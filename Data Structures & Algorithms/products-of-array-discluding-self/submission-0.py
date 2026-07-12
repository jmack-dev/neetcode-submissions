class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods_before = [1 for _ in nums]
        prods_after = [1 for _ in nums]

        for i in range(1,len(nums)):
            prods_before[i] = prods_before[i-1] * nums[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            prods_after[i] = prods_after[i+1] * nums[i+1]

        result = []
        print(prods_before)
        print(prods_after)
        for i in range(len(nums)):
            before = prods_before[i]
            after = prods_after[i] 
            result.append(before*after)
        return result