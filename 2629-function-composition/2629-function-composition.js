/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function (functions) {
  return function (x) {
    functions.reverse();
    functions.forEach((fun)=>{
        x = fun(x)
    })
    return x
  };
};