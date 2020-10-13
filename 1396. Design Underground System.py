import collections


class UndergroundSystem:
    def __init__(self):
        self.users = collections.defaultdict(list)
        self.dest = collections.defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.users[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        prev_station, prev_time = self.users[id]
        self.dest[(prev_station, stationName)].append(t - prev_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return float(
            sum(self.dest[(startStation, endStation)])
            / len(self.dest[(startStation, endStation)])
        )


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
