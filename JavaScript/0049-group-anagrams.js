/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
    const ans = new Map();

    for (const s of strs) {
        const key = s.split("").sort().join("");
        if (!ans.has(key)) {
            ans.set(key, []);
        }
        ans.get(key).push(s);
    }

    return Array.from(ans.values());
};

var strs = ["eat", "tea", "tan", "ate", "nat", "bat"];
console.log(groupAnagrams(strs));
