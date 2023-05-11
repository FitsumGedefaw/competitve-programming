class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        incoming = [0 for _ in range(numCourses)]
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            incoming[course] += 1
            
        queue = deque([course for course in range(numCourses) if incoming[course] == 0])
        totCoursesTaken = len(queue)
        
        while queue:
            course = queue.popleft()
            
            for neigh in graph[course]:
                incoming[neigh] -= 1
                
                if incoming[neigh] == 0:
                    queue.append(neigh)
                    totCoursesTaken += 1
                    
        return totCoursesTaken == numCourses
                    
        