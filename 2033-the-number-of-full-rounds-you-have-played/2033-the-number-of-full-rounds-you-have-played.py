# time complexity: O(1)
# space complexity: O(1)

class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        loginMin = int(loginTime.split(':')[0]) * 60 + int(loginTime.split(':')[1])
        logoutMin = int(logoutTime.split(':')[0]) * 60 + int(logoutTime.split(':')[1])
        if logoutMin < loginMin:  
            logoutMin = logoutMin + 24 * 60
            
        if logoutMin - loginMin < 15:
            return 0
        
        loginMin = loginMin if loginMin % 15 == 0 else loginMin + (15 - loginMin % 15)
        logoutMin = logoutMin if logoutMin % 15 == 0 else logoutMin - (logoutMin % 15)
        
        return (logoutMin - loginMin) // 15


loginTime = "00:31"
logoutTime = "01:14"
print(Solution().numberOfRounds(loginTime, logoutTime))
loginTime = "21:30"
logoutTime = "03:00"
print(Solution().numberOfRounds(loginTime, logoutTime))
loginTime = "00:47"
logoutTime = "00:57"
print(Solution().numberOfRounds(loginTime, logoutTime))
