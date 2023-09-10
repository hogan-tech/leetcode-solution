type FnMemoII = (...params: any) => any;

function createKeyGenerator() {
    let count = 0;
    const map = new Map<unknown, number>();
    return function (input: unknown) {
        if (map.has(input)) return map.get(input);
        map.set(input, ++count);
        return count;
    };
}

function memoize(fn: FnMemoII): FnMemoII {
    const keyGenerator = createKeyGenerator();
    const cache = new Map<string, any>();
    return function (...args) {
        const numbers = args.map(keyGenerator);
        const key = numbers.join(",");
        if (cache.has(key)) return cache.get(key);
        const result = fn(...args);
        cache.set(key, result);
        return result;
    };
}

let callCountII = 0;
const memoizedFnII = memoize(function (a, b) {
    callCountII += 1;
    return a + b;
});
console.log(memoizedFnII(2, 3)); // 5
console.log(memoizedFnII(2, 3)); // 5
console.log(callCountII); // 1
