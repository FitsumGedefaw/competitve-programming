"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def totImportance(graph, emp):
            currImportance = graph[emp][0]
            subordinates = graph[emp][1]
            
            for subord in subordinates:
                currImportance += totImportance(graph, subord)
            
            return currImportance
        
        graph = defaultdict(list)
        for emp in employees:
            graph[emp.id].append(emp.importance)
            graph[emp.id].append(emp.subordinates)
        
                
        return totImportance(graph, id)