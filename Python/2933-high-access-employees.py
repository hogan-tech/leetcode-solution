# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def findHighAccessEmployees(self, accessTimes: List[List[str]]) -> List[str]:
        def timeToMin(time: str):
            hour = time[:2]
            min = time[2:]
            return int(hour) * 60 + int(min)

        employeeDict = defaultdict(list)
        for employee, time in accessTimes:
            employeeDict[employee].append(timeToMin(time))
            if timeToMin(time) < 60:
                employeeDict[employee].append(timeToMin("24" + time[2:]))

            employeeDict[employee].sort()

        result = set()
        for employee, timeList in employeeDict.items():
            if len(timeList) < 3:
                continue
            for i in range(len(timeList) - 2):
                if timeList[i + 2] < timeList[i] + 60:
                    result.add(employee)
        return list(result)


accessTimes = [["a", "0549"], ["b", "0457"],
               ["a", "0532"], ["a", "0621"],
               ["b", "0540"]]
print(Solution().findHighAccessEmployees(accessTimes))
accessTimes = [["d", "0002"], ["c", "0808"],
               ["c", "0829"], ["e", "0215"],
               ["d", "1508"], ["d", "1444"],
               ["d", "1410"], ["c", "0809"]]
print(Solution().findHighAccessEmployees(accessTimes))
accessTimes = [["cd", "1025"], ["ab", "1025"], ["cd", "1046"],
               ["cd", "1055"], ["ab", "1124"], ["ab", "1120"]]
print(Solution().findHighAccessEmployees(accessTimes))
