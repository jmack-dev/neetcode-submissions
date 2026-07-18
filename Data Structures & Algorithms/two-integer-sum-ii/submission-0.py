class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        back = 0
        front = len(numbers) - 1

        while front > back:
            if numbers[front] + numbers[back] == target:
                return [back+1, front+1]
            if numbers[front] + numbers[back] > target:
                front -= 1
            else: 
                back += 1