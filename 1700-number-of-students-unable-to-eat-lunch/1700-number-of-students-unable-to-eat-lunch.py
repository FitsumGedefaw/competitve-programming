class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stus = deque(students)
        sans = deque(sandwiches)
        while stus:
            if stus[0] == sans[0]:
                stus.popleft()
                sans.popleft()
            else:
                k=0
                while stus[0] != sans[0]:
                    k += 1
                    stus.append(stus.popleft())
                    if k == len(stus):
                        return k
        return 0
                    