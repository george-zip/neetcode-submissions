from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        reversed = {}
        for num, count in counts.items():
            reversed.setdefault(count, []).append(num)
        posible_count = len(nums)
        answer = []
        while len(answer) < k:
            if posible_count in reversed:
                answer.extend(reversed[posible_count])
            posible_count -= 1
        return answer