/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n) {
  const result = [];
  const flattening = (arr, n) => {
    for (item of arr) {
      if (Array.isArray(item) && n > 0) {
        flattening(item, n - 1);
      } else {
        result.push(item);
      }
    }
  };
  flattening(arr,n)
  return result;
};