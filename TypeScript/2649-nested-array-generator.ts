type MultidimensionalArray = (MultidimensionalArray | number)[];

function* inorderTraversal(
    arr: MultidimensionalArray
): Generator<number, void, unknown> {
    if (!Array.isArray(arr)) {
        yield arr;
        return;
    }
    for (let i = 0; i < arr.length; i++) {
        yield* inorderTraversal(arr[i] as MultidimensionalArray);
    }
}

const gen1 = inorderTraversal([1, [2, 3]]);
console.log(gen1.next().value); // 1
console.log(gen1.next().value); // 2
console.log(gen1.next().value); // 3
