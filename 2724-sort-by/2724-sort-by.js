/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function (arr, fn) {
  return arr.sort((itemA, itemB) => {
    return fn(itemA) - fn(itemB);
  });
};