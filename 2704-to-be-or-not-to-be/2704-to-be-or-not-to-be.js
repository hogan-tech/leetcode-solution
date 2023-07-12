var expect = function (val) {
  return {
    toBe: function (expected) {
      if (val !== expected) {
        throw new Error("Not Equal");
      }
      return true;
    },
    notToBe: function (expected) {
      if (val === expected) {
        throw new Error("Equal");
      }
      return true;
    },
  };
};


