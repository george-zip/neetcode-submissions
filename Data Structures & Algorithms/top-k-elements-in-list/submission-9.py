from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_list = Counter(nums)
        numbers_by_frequency = defaultdict(list)
        max_val = 0
        for num, frequency in frequency_list.items():
            numbers_by_frequency[frequency].append(num)
            max_val = max(max_val, frequency)
        answer = []
        for i in range(max_val, 0, -1):
            for num in numbers_by_frequency.get(i, []):
                answer.append(num)
                if len(answer) == k:
                    return answer
    
        
