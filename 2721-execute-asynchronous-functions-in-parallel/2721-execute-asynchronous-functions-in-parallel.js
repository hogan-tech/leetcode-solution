/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = async function (functions) {
  return new Promise((resolve, reject) => {
    if (functions.length === 0) {
      resolve([]);
      return;
    }

    const res = new Array(functions.length).fill(null);

    let resolvedCount = 0;

    functions.forEach(async (element, idx) => {
      try {
        const subRes = await element();
        res[idx] = subRes;
        resolvedCount++;
        if (resolvedCount === functions.length) {
          return resolve(res);
        }
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