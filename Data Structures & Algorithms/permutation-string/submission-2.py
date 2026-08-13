from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        char_dict = defaultdict(int)
        for s in s1:
            char_dict[s] += 1
        window_size = len(s1)
        total_char = 0
        substr_char_dict = defaultdict(int)
        for i in range(len(s2)):
            if s2[i] in char_dict:
                substr_char_dict[s2[i]] += 1
            total_char += 1
            if total_char > window_size:
                if s2[i-window_size] in char_dict:
                    substr_char_dict[s2[i-window_size]] -= 1
                total_char -= 1
            if substr_char_dict == char_dict:
                return True
        return False