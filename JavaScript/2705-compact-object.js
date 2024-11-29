var compactObject = function (obj) {
  function dfs(obj) {
    if (!obj) return;
    if (typeof obj !== "object") {
      return obj;
    }
    if (Array.isArray(obj)) {
      const newArray = [];
      for (let i = 0; i < obj.length; i++) {
        const subRes = dfs(obj[i]);
        if (subRes) newArray.push(subRes);
      }
      return newArray;
    }

    const newObj = {};
    for (const key in obj) {
      const subRes = dfs(obj[key]);
      if (subRes) {
        newObj[key] = subRes;
      }
    }
    return newObj
  }
  return dfs(obj);
};