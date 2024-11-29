function* fibGenerator(): Generator<number, any, number> {
	yield 0
	yield 1
    let fibCache = [0, 1];
    let count = 1;
    while (true) {
        fibCache.push(fibCache[count] + fibCache[count - 1]);
        count++;
        yield fibCache[count];
    }
}

const gen = fibGenerator();
console.log(gen.next().value); 
console.log(gen.next().value); 
console.log(gen.next().value); 
console.log(gen.next().value); 
console.log(gen.next().value); 
console.log(gen.next().value); 
