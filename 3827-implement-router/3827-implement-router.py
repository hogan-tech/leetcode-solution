# time complexity: O(nlogn)
# space complexity: O(n)
from bisect import bisect_left, bisect_right, insort
from collections import defaultdict, deque
from typing import List


class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()
        self.packetSet = set()
        self.destinationMap = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packetSet:
            return False

        if len(self.queue) == self.memoryLimit:
            prevSource, prevDestination, prevTimestamp = self.queue.popleft()
            self.packetSet.remove((prevSource, prevDestination, prevTimestamp))
            timestamps = self.destinationMap[prevDestination]
            idx = bisect_left(timestamps, prevTimestamp)
            if 0 <= idx < len(timestamps) and timestamps[idx] == prevTimestamp:
                timestamps.pop(idx)

        self.queue.append(packet)
        self.packetSet.add(packet)
        insort(self.destinationMap[destination], timestamp)

        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []

        source, destination, timestamp = self.queue.popleft()
        self.packetSet.remove((source, destination, timestamp))

        timestamps = self.destinationMap[destination]
        idx = bisect_left(timestamps, timestamp)
        if 0 <= idx < len(timestamps) and timestamps[idx] == timestamp:
            timestamps.pop(idx)
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.destinationMap[destination]
        left = bisect_left(timestamps, startTime)
        right = bisect_right(timestamps, endTime)
        return right - left


router1 = Router(3)
print(router1.addPacket(1, 4, 90))
print(router1.addPacket(2, 5, 90))
print(router1.addPacket(1, 4, 90))
print(router1.addPacket(3, 5, 95))
print(router1.addPacket(4, 5, 105))
print(router1.forwardPacket())
print(router1.addPacket(5, 2, 110))
print(router1.getCount(5, 100, 110))


router2 = Router(2)
print(router2.addPacket(7, 4, 90))
print(router2.forwardPacket())
print(router2.forwardPacket())
