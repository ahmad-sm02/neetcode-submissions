class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        nums_len = len(nums)
        for i, num in enumerate(nums):
            if i and num == nums[i-1]:
                continue
            j, k = i + 1, nums_len - 1
            while j < k:
                curr_sum = num + nums[j] + nums[k]
                if curr_sum < 0:
                    j += 1
                elif curr_sum > 0:
                    k -= 1
                else:
                    res.append([num, nums[j], nums[k]])
                    curr_k_num = nums[k]
                    k -= 1
                    while k > 0 and curr_k_num == nums[k]:
                        k -= 1
        return res

        