# time complexity: O(V+E)
# space complexity: O(V)
from collections import Counter, defaultdict
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = Counter()
        available = set(supplies)
        adjList = defaultdict(set)
        result = []
        for recipe, ingredient in zip(recipes, ingredients):
            nonAvaible = 0
            for item in ingredient:
                if item not in available:
                    nonAvaible += 1
                    adjList[item].add(recipe)
            if nonAvaible == 0:
                result.append(recipe)
            else:
                indegree[recipe] = nonAvaible

        for item in result:
            for recipe in adjList.pop(item, set()):
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    result.append(recipe)
        return result


recipes = ["bread"]
ingredients = [["yeast", "flour"]]
supplies = ["yeast", "flour", "corn"]
print(Solution().findAllRecipes(recipes, ingredients, supplies))

recipes = ["bread", "sandwich"]
ingredients = [["yeast", "flour"], ["bread", "meat"]]
supplies = ["yeast", "flour", "meat"]
print(Solution().findAllRecipes(recipes, ingredients, supplies))

recipes = ["bread", "sandwich", "burger"]
ingredients = [["yeast", "flour"], [
    "bread", "meat"], ["sandwich", "meat", "bread"]]
supplies = ["yeast", "flour", "meat"]
print(Solution().findAllRecipes(recipes, ingredients, supplies))
