class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        queue = deque([*rooms[0]])
        
        while queue:
            print(queue)
            nextRooms = []
            while queue:
                room = queue.popleft()
                visited.add(room)
                
                for nextRoom in rooms[room]:
                    if nextRoom not in visited:
                        nextRooms.append(nextRoom)
                
            queue = deque(nextRooms)
        
        return len(visited) == len(rooms)
        