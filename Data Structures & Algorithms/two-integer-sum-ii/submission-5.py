class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums_len = len(numbers)
        i, j = 0, nums_len-1
        while i < j:
            nums_sum = numbers[i] + numbers[j]
            if nums_sum > target:
                j -= 1
            elif nums_sum < target:
                i += 1
            else:
                return [i+1, j+1]
        return False
        