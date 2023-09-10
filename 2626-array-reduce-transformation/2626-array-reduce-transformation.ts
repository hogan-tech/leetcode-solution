type FnCus = (accum: number, curr: number) => number;

function reduce(nums: number[], fn: FnCus, init: number): number {
    for (const item of nums) {
        init = fn(init, item);
    }
    return init;
}

const Nums = [1, 2, 3, 4];
const Func: FnCus = function sum(accum: number, curr: number) {
    return accum + curr * curr;
};
const Init = 100;

console.log(reduce(Nums, Func, Init));
