from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = [[] for _ in range(len(nums) + 1)]
        counts = Counter(nums)
        for num, count in counts.items():
            frequencies[count].append(num)
        results = []
        for i in range(len(frequencies) - 1, -1, -1):
            if frequencies[i]:
                results.extend(frequencies[i])
            if len(results) == k:
                break
        return results