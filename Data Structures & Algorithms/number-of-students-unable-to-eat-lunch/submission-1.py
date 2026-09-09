class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        preferences = [0, 0]
        for sandwich_pref in students:
            preferences[sandwich_pref] += 1
        for actual_sandwich in sandwiches:
            if preferences[actual_sandwich] == 0:
                break
            preferences[actual_sandwich] -= 1
        return sum(preferences)