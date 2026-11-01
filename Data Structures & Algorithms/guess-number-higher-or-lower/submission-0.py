# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        pick = high // 2
        while result := guess(pick):
            if result == 1:
                low = pick + 1
            else:
                high = pick - 1
            pick = low + (high - low) // 2
        return pick