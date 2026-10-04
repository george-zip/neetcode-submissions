from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        preferences = Counter(students)
        for sandwich in sandwiches:
            if preferences[sandwich] > 0:
                preferences[sandwich] -= 1
            else:
                break
        return sum(preferences.values())
                