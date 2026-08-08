class Solution:
    def fix_zeros(self, nums, i):
        prd = 1
        for j, num in enumerate(nums):
            if i == j:
                continue
            prd *= num
        return prd

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_prd = 1
        for num in nums:
            nums_prd *= num
        out_nums = [nums_prd] * len(nums)
        for i, num in enumerate(nums):
            if num == 0:
                out_nums[i] = self.fix_zeros(nums, i)
            else:
                out_nums[i] //= num
        return out_nums