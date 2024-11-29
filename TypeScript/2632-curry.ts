function curry(fn: Function): Function {
    return function curried(...args: any) {
		if(args.length >= fn.length){
			return fn(...args)
		}
        return (...nextArgs: any) => {
            return curried(...args, ...nextArgs);
        };
    };
}

function sum(a: number, b: number) {
    return a + b;
}
const csum = curry(sum);
console.log(csum(1)(2)); // 3
