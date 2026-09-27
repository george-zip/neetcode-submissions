from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = Counter(nums)
        inverse_frequencies = [[] for _ in range(len(nums) + 1)]
        for num, frequency in frequency_map.items():
            inverse_frequencies[frequency].append(num)
        answer = []
        for i in range(len(inverse_frequencies) - 1, -1, -1):
            for num in inverse_frequencies[i]:
                answer.append(num)
                k -= 1
                if not k:
                    return answer
        return answer
            