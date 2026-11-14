from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        q = deque() # this store indices
        left = 0
        for right, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(right)

            if q[0] < left:
                q.popleft()

            if right + 1 >= k:
                answer.append(nums[q[0]])
                left += 1

        return answer
        
