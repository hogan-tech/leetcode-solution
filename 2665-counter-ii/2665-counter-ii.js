var createCounter = function (init) {
  const original_number = init;
  return {
    increment: () => {
      return ++init;
    },
    decrement: () => {

      return --init;
    },
    reset: () => {
      init = original_number;
      return init;
    },
  };
};