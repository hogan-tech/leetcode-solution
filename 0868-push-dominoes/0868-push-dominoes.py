# time complexity: O(n)
# space complexity: O(n)
class Solution(object):
    def pushDominoes(self, dominoes):
        N = len(dominoes)
        force = [0] * N

        f = 0
        for i in range(N):
            if dominoes[i] == 'R':
                f = N
            elif dominoes[i] == 'L':
                f = 0
            else:
                f = max(f-1, 0)
            force[i] += f

        f = 0
        for i in range(N-1, -1, -1):
            if dominoes[i] == 'L':
                f = N
            elif dominoes[i] == 'R':
                f = 0
            else:
                f = max(f-1, 0)
            force[i] -= f

        return "".join('.' if f == 0 else 'R' if f > 0 else 'L'
                       for f in force)


dominoes = "RR.L"
print(Solution().pushDominoes(dominoes))
dominoes = ".L.R...LR..L.."
print(Solution().pushDominoes(dominoes))
