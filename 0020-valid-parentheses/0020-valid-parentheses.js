/**
 * @param {string} s
 * @return {boolean}
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
var isValid = function(s) {
    const bracketMap = { "(": ")", "[": "]", "{": "}" };
    const openSet = new Set(["(", "[", "{"]);
    const stack = [];
    
    for (let char of s) {
        if (openSet.has(char)) {
            stack.push(char);
        } else if (stack.length > 0 && char === bracketMap[stack[stack.length - 1]]) {
            stack.pop();
        } else {
            return false;
        }
    }
    
    return stack.length === 0;
};

const input = "(())";
console.log(isValid(input)); // Output will be true or false based on the validity of the parentheses.
