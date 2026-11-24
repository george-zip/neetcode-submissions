class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        temp_by_day = []
        for idx, temp in enumerate(temperatures):
            while temp_by_day and temp > temp_by_day[-1][0]:
                _, prev_idx = temp_by_day.pop()
                answer[prev_idx] = idx - prev_idx
            temp_by_day.append((temp, idx))
        return answer

