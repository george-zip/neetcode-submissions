class Solution:

    def box_num(cls, num):
        if num < 3:
            return 0
        elif num < 6:
            return 1
        else:
            return 2

    def sub_box_num(cls, row_num, col_num):
        return cls.box_num(row_num), cls.box_num(col_num)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [set() for _ in range(9)]
        sub_boxes = [[set() for _ in range(3)] for _ in range(3)]
        for row_num, row in enumerate(board):
            current_row = set()
            for col_num, num in enumerate(row):
                if num == ".":
                    continue
                if num in current_row:
                    return False
                current_row.add(num)
                if num in columns[col_num]:
                    return False
                columns[col_num].add(num)
                box_row, box_col = self.sub_box_num(row_num, col_num)
                if num in sub_boxes[box_row][box_col]:
                    return False
                sub_boxes[box_row][box_col].add(num)
        return True
