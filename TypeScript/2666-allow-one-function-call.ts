type Fn1 = (...args: any[]) => any

function once(fn: Fn1): Fn1 {
    let flag = false;
    return function (...args) {
        if (flag) {
            return undefined;
        } else {
            flag = true;
            return fn(...args);
        }
    };
}

let fn1: Fn1 = (a, b, c) => a + b + c;
let onceFn = once(fn1);
console.log(onceFn(1, 2, 3)); // 6
console.log(onceFn(2, 3, 6)); // returns undefined without calling fn
