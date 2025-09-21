# time complexity: O(eloge + qloge)
# space complexity: O(e)
from typing import List


class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.available = {}
        self.movieShops = {}
        self.rented = set()

        for shop, movie, price in entries:
            self.available[(shop, movie)] = price
            if movie not in self.movieShops:
                self.movieShops[movie] = []
            self.movieShops[movie].append((price, shop))

        for movie in self.movieShops:
            self.movieShops[movie].sort()

    def search(self, movie: int) -> List[int]:
        result = []
        for _, shop in self.movieShops.get(movie, []):
            if (shop, movie) not in self.rented:
                result.append(shop)
            if len(result) == 5:
                break
        return result

    def rent(self, shop: int, movie: int) -> None:
        self.rented.add((shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.rented.discard((shop, movie))

    def report(self) -> List[List[int]]:
        rentedList = []
        for shop, movie in self.rented:
            price = self.available[(shop, movie)]
            rentedList.append((price, shop, movie))

        rentedList.sort()
        return [[shop, movie] for _, shop, movie in rentedList[:5]]


movieRentingSystem = MovieRentingSystem(
    3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]])
movieRentingSystem.search(1)
movieRentingSystem.rent(0, 1)
movieRentingSystem.rent(1, 2)
movieRentingSystem.report()
movieRentingSystem.drop(1, 2)
movieRentingSystem.search(2)
