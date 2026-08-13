from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        char_dict = defaultdict(int)
        for s in s1:
            char_dict[s] += 1
        window_size = len(s1)
        for i in range(len(s2)):
            if s2[i] not in char_dict:
                continue
            substr = s2[i:i+window_size]
            substr_char_dict = defaultdict(int)
            for s in substr:
                substr_char_dict[s] += 1
            if substr_char_dict == char_dict:
                return True
        return False