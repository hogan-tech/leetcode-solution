# time complexity: O(1)
# space complexity: O(n)
from collections import defaultdict


class FrequencyTracker:
    def __init__(self):
        self.numFreq = defaultdict(int)
        self.freqNums = defaultdict(set)

    def add(self, number: int) -> None:
        if self.numFreq[number]:
            currFreq = self.numFreq[number]
            self.freqNums[currFreq].remove(number)
        self.numFreq[number] += 1
        currFreq = self.numFreq[number]
        self.freqNums[currFreq].add(number)

    def deleteOne(self, number: int) -> None:
        if self.numFreq[number] > 0:
            currFreq = self.numFreq[number]
            self.freqNums[currFreq].remove(number)
            if not self.freqNums[currFreq]:
                del self.freqNums[currFreq]
            self.numFreq[number] -= 1
            if self.numFreq == 0:
                del self.numFreq[number]
            else:
                newFreq = self.numFreq[number]
                self.freqNums[newFreq].add(number)

    def hasFrequency(self, frequency: int) -> bool:
        return len(self.freqNums[frequency]) > 0


frequencyTracker1 = FrequencyTracker()
frequencyTracker1.add(3)
frequencyTracker1.add(3)
print(frequencyTracker1.hasFrequency(2))


frequencyTracker2 = FrequencyTracker()
frequencyTracker2.add(1)
frequencyTracker2.deleteOne(1)
print(frequencyTracker2.hasFrequency(1))


frequencyTracker3 = FrequencyTracker()
print(frequencyTracker3.hasFrequency(2))
frequencyTracker3.add(3)
print(frequencyTracker3.hasFrequency(1))
