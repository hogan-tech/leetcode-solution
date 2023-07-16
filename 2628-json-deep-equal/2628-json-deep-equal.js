/**
 * @param {any} o1
 * @param {any} o2
 * @return {boolean}
 */
const helper = (key,value) => {
    return (value && !Array.isArray(value) && typeof value === "object")
    ? Object.fromEntries(Object.entries(value).sort())
    : value;
};

let areDeeplyEqual = function (o1, o2) {
    console.log(JSON.stringify(o1, helper))
    console.log(JSON.stringify(o2, helper))
  return JSON.stringify(o1, helper) === JSON.stringify(o2, helper);
};