/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function (arr, fn) {
  result = [];
  arr.forEach((num, i) => {
    if (fn(num, i)) {
      result.push(num);
    }
  });
  return result;
};