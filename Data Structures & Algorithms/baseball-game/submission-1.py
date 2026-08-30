def is_int(s):
    try:
        x = int(s)
        return True
    except ValueError:
        return False

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        vals = []
        for op in operations:
            print(f"op = {op}")
            print(f"vals = {vals}")
            if is_int(op):
                vals.append(int(op))
            elif op == "+":
                vals.append(vals[-2] + vals[-1])
            elif op == "D":
                vals.append(2 * vals[-1])
            else:
                vals.pop()
            print(5 * "x")
        return sum(vals)
        