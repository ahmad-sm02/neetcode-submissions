from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1
        sorted_dict = dict(sorted(freq_dict.items(), key=lambda i: i[1]))
        res = []
        for i in range(k):
            res.append(sorted_dict.popitem()[0])
        return res        