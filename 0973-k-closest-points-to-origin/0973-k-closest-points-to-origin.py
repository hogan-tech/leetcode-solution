class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda Item: Item[0] ** 2 + Item[1]**2)
        return points[:k]