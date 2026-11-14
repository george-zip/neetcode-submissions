from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_list = Counter(nums)
        numbers_by_frequency = defaultdict(list)
        max_val = 0
        # print(frequency_list)
        for num, frequency in frequency_list.items():
            numbers_by_frequency[frequency].append(num)
            max_val = max(max_val, frequency)
        # print(numbers_by_frequency)
        answer = []
        for i in range(max_val, -1, -1):
            print(i)
            if i in numbers_by_frequency:
                answer.extend(numbers_by_frequency[i])
            if len(answer) == k:
                break
        return answer
        
