/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function (arr1, arr2) {
  const merge = {};
  for (item of arr1.concat(arr2)) {
    merge[item.id] = merge[item.id]
      ? { ...merge[item.id], ...item }
      : { ...item };
  }
  return Object.values(merge);
};