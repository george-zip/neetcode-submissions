from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        top_k = sorted(counts.items(), key=lambda c: c[1], reverse=True)[:k]
        return [item[0] for item in top_k]