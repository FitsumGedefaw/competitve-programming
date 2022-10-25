class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                k = 0
                while students[0] != sandwiches[0]:
                    k += 1
                    students.append(students.pop(0))
                    if k == len(students):
                        return k
        return 0
                    