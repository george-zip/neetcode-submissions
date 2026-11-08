from typing import List

class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        if len(a) > len(b):
            a, b = b, a

        m, n = len(a), len(b)

        if m + n == 0:
            raise ValueError("At least one array must be nonempty")

        left_size = (m + n + 1) // 2
        lo, hi = 0, m

        while lo <= hi:
            i = (lo + hi) // 2
            j = left_size - i

            a_left = a[i - 1] if i > 0 else float("-inf")
            a_right = a[i] if i < m else float("inf")

            b_left = b[j - 1] if j > 0 else float("-inf")
            b_right = b[j] if j < n else float("inf")

            if a_left <= b_right and b_left <= a_right:
                if (m + n) % 2 == 1:
                    return max(a_left, b_left)

                return (
                    max(a_left, b_left)
                    + min(a_right, b_right)
                ) / 2

            elif a_left > b_right:
                hi = i - 1
            else:
                lo = i + 1

