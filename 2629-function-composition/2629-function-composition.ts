type Func = (x: number) => number;

function compose(functions: Func[]): Func {
    return function (x) {
		functions.reverse().forEach((func)=>{
			x = func(x)
		})
        return x;
    };
}

const fn = compose([(x) => x + 1, (x) => 2 * x]);
console.log(fn(4)); // 9
