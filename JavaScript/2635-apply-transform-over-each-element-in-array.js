/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function (arr, fn) {
  arr = arr.map((num, i) => {
    return fn(num, i);
  });
  return arr;
};