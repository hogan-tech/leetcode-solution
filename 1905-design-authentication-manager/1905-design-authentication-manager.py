from collections import defaultdict


class AuthenticationManager(object):

    def __init__(self, timeToLive: int):
        self.token = defaultdict(int)
        self.time = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        limit = currentTime-self.time
        if tokenId in self.token and self.token[tokenId] > limit:
            self.token[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        limit = currentTime-self.time
        count = 0
        for i in self.token:
            if self.token[i] > limit:
                count += 1
        return count


authenticationManager = AuthenticationManager(5)
authenticationManager.renew("aaa", 1)
authenticationManager.generate("aaa", 2)
print(authenticationManager.countUnexpiredTokens(6))
authenticationManager.generate("bbb", 7)
authenticationManager.renew("aaa", 8)
authenticationManager.renew("bbb", 10)
print(authenticationManager.countUnexpiredTokens(15))
