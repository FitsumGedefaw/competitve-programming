class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.travelTime = defaultdict(list)        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startCity, startTime = self.checkin[id]
        self.travelTime[(startCity, stationName)].append(t - startTime)        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.travelTime[(startStation, endStation)]) / len(self.travelTime[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)