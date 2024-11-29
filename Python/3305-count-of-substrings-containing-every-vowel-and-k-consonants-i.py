# time cmplexity: O(n^2)
# space complexity: O(1)
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set('aeiou')
        n = len(word)

        def satisfyVowels(vowelCount):
            return all(vowelCount[vowel] > 0 for vowel in vowels)

        count = 0
        for left in range(n):
            vowelCount = {v: 0 for v in vowels}
            consonantCount = 0
            for right in range(left, n):
                char = word[right]
                if char in vowels:
                    vowelCount[char] += 1
                else:
                    consonantCount += 1
                if consonantCount > k:
                    break
                if satisfyVowels(vowelCount) and consonantCount == k:
                    count += 1
        return count


word = "aeioqq"
k = 1
print(Solution().countOfSubstrings(word, k))
