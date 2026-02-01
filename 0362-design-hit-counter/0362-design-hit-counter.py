class HitCounter:

    def __init__(self):
        self.timestampList = []

    def hit(self, timestamp: int) -> None:
        self.timestampList.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        preTimestamp = timestamp - 300
        count = 0
        for time in self.timestampList:
            if preTimestamp < time <= timestamp:
                count += 1
        return count


hitCounter = HitCounter()
hitCounter.hit(1)
hitCounter.hit(2)
hitCounter.hit(3)
print(hitCounter.getHits(4))
hitCounter.hit(300)
print(hitCounter.getHits(300))
print(hitCounter.getHits(301))
