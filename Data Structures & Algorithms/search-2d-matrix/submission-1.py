def row_and_col(num, col_count):
    return num // col_count, num % col_count

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) * len(matrix[0]) - 1
        cols = len(matrix[0])
        while lo <= hi:
            mid = (lo + hi) // 2
            row, col = row_and_col(mid, cols)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return False 
        