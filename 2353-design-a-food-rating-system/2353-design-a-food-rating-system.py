from heapq import heappush, heappop
from collections import defaultdict
from typing import List

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self._cuisines = cuisines
        self._ratings = ratings
        self._heaps = defaultdict(list)
        for i, (f, c, r) in enumerate(zip(foods, cuisines, ratings)):
            heappush(self._heaps[c], (-r, f, i))

        self._food_idxs = {f: i for i, f in enumerate(foods)}

    def changeRating(self, food: str, newRating: int) -> None:
        idx = self._food_idxs[food]
        self._ratings[idx] = newRating
        cuisine = self._cuisines[idx]
        heappush(self._heaps[cuisine], (-newRating, food, idx))

    def highestRated(self, cuisine: str) -> str:
        neg_rating, food, idx = self._heaps[cuisine][0]
        while -neg_rating != self._ratings[idx]:
            heappop(self._heaps[cuisine])
            neg_rating, food, idx = self._heaps[cuisine][0]

        return food


foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
ratings = [9, 12, 8, 15, 14, 7]

obj = FoodRatings(foods, cuisines, ratings)
