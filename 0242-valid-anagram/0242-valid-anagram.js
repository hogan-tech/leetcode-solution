/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    // Helper function to create a character counter
    const getCharacterCount = (str) => {
        const counter = new Map();
        for (const char of str) {
            counter.set(char, (counter.get(char) || 0) + 1);
        }
        return counter;
    };

    // Helper function to check if two counters are equal
    const isCounterEqual = (counter1, counter2) => {
        if (counter1.size !== counter2.size) {
            return false;
        }
        for (const [key, value] of counter1) {
            if (counter2.get(key) !== value) {
                return false;
            }
        }
        return true;
    };

    // Use the Counter approach to check if s and t are anagrams
    const counterS = getCharacterCount(s);
    const counterT = getCharacterCount(t);
    return isCounterEqual(counterS, counterT);
};

// Example usage:
console.log(isAnagram("anagram", "nagaram")); // Output: true
console.log(isAnagram("rat", "car")); // Output: false
