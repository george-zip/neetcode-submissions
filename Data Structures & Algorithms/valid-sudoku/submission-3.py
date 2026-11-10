class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [set() for _ in range(len(board))]
        sub_boxes = [[set() for _ in range(3)] for _ in range(3)]
        for row_idx, row in enumerate(board):
            current_row = set()
            for col_idx, cell_val in enumerate(row):
                if cell_val == ".":
                    continue
                print(f"{row_idx=},{col_idx=},{cell_val=}")
                if cell_val in current_row:
                    print(1)
                    return False
                current_row.add(cell_val)
                if cell_val in columns[col_idx]:
                    print(2)
                    return False
                columns[col_idx].add(cell_val)
                if cell_val in sub_boxes[row_idx // 3][col_idx // 3]:
                    print(3)
                    return False
                sub_boxes[row_idx // 3][col_idx // 3].add(cell_val)
        return True
