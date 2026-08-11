class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        elif len(s) == 1: return 1
        l = 0
        unique_dict = {}
        max_length = 0
        for r in range(len(s)):
            if s[r] in unique_dict:
                l = max(unique_dict[s[r]]+1, l)
            unique_dict[s[r]] = r
            max_length = max(r-l+1, max_length)
        return max_length



        