from collections import defaultdict


class Leaderboard:

    def __init__(self):
        self.scores = defaultdict()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = 0
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        values = [v for _, v in sorted(
            self.scores.items(), key=lambda item: item[1])]
        values.sort(reverse=True)
        total, i = 0, 0
        while i < K:
            total += values[i]
            i += 1

        return total

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0


leaderboard = Leaderboard()
leaderboard.addScore(1, 73)
leaderboard.addScore(2, 56)
leaderboard.addScore(3, 39)
leaderboard.addScore(4, 51)
leaderboard.addScore(5, 4)
leaderboard.top(1)
leaderboard.reset(1)
leaderboard.reset(2)
leaderboard.addScore(2, 51)
leaderboard.top(3)
