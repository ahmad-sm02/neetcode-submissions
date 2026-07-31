from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_freq_dict = defaultdict(int)
        for i in range(len(s)):
            char_freq_dict[s[i]] += 1
            char_freq_dict[t[i]] -= 1
        if any(char_freq_dict.values()):
            return False
        else:
            return True

        