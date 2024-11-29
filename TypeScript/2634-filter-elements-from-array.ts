function filter(arr: number[], fn: (n: number, i: number) => any): number[] {
    const result:number[] = []
	arr.forEach((item,index)=>{
		if(fn(item,index)){
			result.push(item)
		}
	})
    return result;
}

const Arr = [10, 20, 30];
const Fn = function firstIndex(n:number, i:number) { return i === 0; }

console.log(filter(Arr, Fn));
