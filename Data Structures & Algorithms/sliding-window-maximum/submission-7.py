from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        q = deque()
        left = 0
        for right, num in enumerate(nums):
            while q and num > nums[q[-1]]:
                q.pop()
            q.append(right)

            if left > q[0]:
                q.popleft()

            if right - left + 1 >= k:
                answer.append(
                    nums[q[0]]
                )
                left += 1
        return answer