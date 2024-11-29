var expect = function (val) {
  return {
    toBe: function (expected) {
      if (expected !== val) throw new Error("Not Equal");
      return true;
    },
    notToBe: function (expected) {
      if (expected === val) throw new Error("Equal");
      return true;
    },
  };
};