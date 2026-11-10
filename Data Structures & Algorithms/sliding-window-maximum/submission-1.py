class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window_max = max(nums[:k])  
        answer = [window_max]
        left = 0
        for right in range(k, len(nums)):
            new_val = nums[right]
            old_val = nums[left]
            left += 1
            if new_val > window_max:
                window_max = new_val
            elif old_val == window_max:
                window_max = max(nums[left:right + 1])
            answer.append(window_max)
        return answer
