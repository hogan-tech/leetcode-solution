from collections import Counter
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circleStudents = 0
        squareStudents = 0
        for student in students:
            if student == 0:
                circleStudents += 1
            else:
                squareStudents += 1
        for sandwich in sandwiches:
            if sandwich == 0 and circleStudents == 0:
                return squareStudents
            if sandwich == 1 and squareStudents == 0:
                return circleStudents
            if sandwich == 0:
                circleStudents -= 1
            else:
                squareStudents -= 1
        return 0


students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]
print(Solution().countStudents(students, sandwiches))
