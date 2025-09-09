# time complexity: O(n)
# space complexity: O(n)
from collections import deque


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        sharing = 0
        delayQue = deque([1])
        forgetQue = deque([1])
        for _ in range(n - 1):
            if len(delayQue) >= delay:
                sharing = (sharing + delayQue.popleft()) % MOD
            if len(forgetQue) >= forget:
                sharing = (sharing - forgetQue.popleft()) % MOD
            delayQue.append(sharing)
            forgetQue.append(sharing)
        print(delayQue, forgetQue)
        return sum(forgetQue) % MOD


n = 6
delay = 2
forget = 4
print(Solution().peopleAwareOfSecret(n, delay, forget))
'''
Day 1: Suppose the first person is named A. (1 person)
Day 2: A is the only person who knows the secret. (1 person)
Day 3: A shares the secret with a new person, B. (2 people)
Day 4: A shares the secret with a new person, C. (3 people)
Day 5: A forgets the secret, and B shares the secret with a new person, D. (3 people)
Day 6: B shares the secret with E, and C shares the secret with F. (5 people)

Day 1: A
Day 2: A
Day 3: AB
Day 4: AC B
Day 5: X BD C 
Day 6: X BE CF D
'''
n = 4
delay = 1
forget = 3
print(Solution().peopleAwareOfSecret(n, delay, forget))
'''
Day 1: The first person is named A. (1 person)
Day 2: A shares the secret with B. (2 people)
Day 3: A and B share the secret with 2 new people, C and D. (4 people)
Day 4: A forgets the secret. B, C, and D share the secret with 3 new people. (6 people)

Day 1: A
Day 2: AB
Day 3: AC BD
Day 4: BE CF DH
'''
