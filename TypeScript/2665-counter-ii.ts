type ReturnObj = {
    increment: () => number;
    decrement: () => number;
    reset: () => number;
};

function createCounter(init: number): ReturnObj {
    let value = init;
    return {
        increment: () => value+=1,
        decrement: () => value-=1,
        reset: () => value = init,
    };
}

const counter1 = createCounter(5);
console.log(counter1.increment()); // 6
console.log(counter1.reset()); // 5
console.log(counter1.decrement()); // 4
