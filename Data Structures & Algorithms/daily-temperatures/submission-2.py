class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        temp_stack = []
        for i, temp in enumerate(temperatures):
            while temp_stack and temp > temp_stack[-1][0]:
                _, j = temp_stack.pop()
                result[j] = i - j
            temp_stack.append((temp, i))
        return result