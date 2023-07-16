/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = async function (functions) {
  return new Promise((resolve, reject) => {
    if (functions.length == 0) {
      resolve([]);
      return;
    }

    const res = Array(functions.length).fill(null);
    let resolvedCount = 0;
    functions.forEach(async (item, idx) => {
      try {
        const subRes = await item();
        res[idx] = subRes;
        resolvedCount++;
        if (resolvedCount === functions.length) return resolve(res);
      } catch (err) {
        reject(err);
      }
    });
  });
};
/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */