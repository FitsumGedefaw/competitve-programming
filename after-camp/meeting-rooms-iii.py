class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetingCt =  defaultdict(int)
        maxCt = 0
        freeRooms = [i for i in range(n)]
        heapq.heapify(freeRooms)
        takenRooms = []
        meetings.sort()

        for start, end in meetings:
            #print([start, end], rooms)
            
            while takenRooms and takenRooms[0][0] <= start:
                heapq.heappush(freeRooms, heapq.heappop(takenRooms)[1])
            
            
            if not freeRooms:
                roomFinishTime, roomNo = heapq.heappop(takenRooms)
            else:
                roomNo = heapq.heappop(freeRooms)
                roomFinishTime = start

            #print((roomFinishTime, roomNo))
            meetingCt[roomNo] += 1
            maxCt = max(maxCt, meetingCt[roomNo])
            nextRoomFinishTime = max(roomFinishTime, start) + end - start 
            heapq.heappush(takenRooms, (nextRoomFinishTime, roomNo))
        
        #print("max", maxCt)
        #print(meetingCt)
        ans = n
        for room in meetingCt:
            if meetingCt[room] == maxCt and room < ans:
                ans = room
        
        return ans

        