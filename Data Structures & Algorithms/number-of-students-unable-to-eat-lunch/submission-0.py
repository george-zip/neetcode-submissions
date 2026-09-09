class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        prefer_circular = 0
        prefer_square = 0
        for student in students:
            print(student == 0)
            if student == 0:
                prefer_circular += 1
            else:
                prefer_square += 1
        for sammie in sandwiches:
            if sammie == 0:
                if prefer_circular:
                    prefer_circular -= 1
                else:
                    break
            else:
                if prefer_square:
                    prefer_square -= 1
                else:
                    break
        return prefer_circular + prefer_square