class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_boxes = [[set() for _ in range(3)] for _ in range(3)]
        columns = [set() for _ in range(9)]
        for row_idx in range(len(board)):
            row = set()
            for col_idx, val in enumerate(board[row_idx]):
                if val == ".":
                    continue
                if val in row:
                    # print(f"{val} in row {row_idx}")
                    return False
                row.add(val)
                if val in columns[col_idx]:
                    # print(f"{val} in {col_idx}")
                    return False
                columns[col_idx].add(val)
                if val in sub_boxes[row_idx // 3][col_idx // 3]:
                    # print(f"{val} in {row_idx // 3},{col_idx // 3}")
                    return False
                sub_boxes[row_idx // 3][col_idx // 3].add(val)
        return True