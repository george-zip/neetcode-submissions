from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = [[] for _ in range(len(nums) + 1)]
        counts = Counter(nums)
        for num, count in counts.items():
            frequencies[count].append(num)
        results = []
        for i in range(len(frequencies) - 1, -1, -1):
            for num in frequencies[i]:
                results.append(num)
                if len(results) == k:
                    return results
        return results