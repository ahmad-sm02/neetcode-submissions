class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_sequence = 0
        for num in num_set:
            if num-1 in num_set:
                continue
            seq_len = 0
            curr_num = num
            while curr_num in num_set:
                seq_len += 1
                curr_num += 1
            longest_sequence = max(longest_sequence, seq_len)
        return longest_sequence
        