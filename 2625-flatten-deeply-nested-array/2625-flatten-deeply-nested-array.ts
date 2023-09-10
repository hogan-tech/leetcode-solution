type MultiDimensionalArray = (number | MultiDimensionalArray)[];

var flat = function (
    arr: MultiDimensionalArray,
    n: number
): MultiDimensionalArray {
    const result: MultiDimensionalArray = [];
    if (n === 0) return arr;

    const flatting = (array: MultiDimensionalArray, left: number) => {
        for (const item of array) {
            if (Array.isArray(item) && left > 0) {
                flatting(item, left - 1);
            } else {
                result.push(item);
            }
        }
    };
    flatting(arr, n);
    return result;
};

const array = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]];
const n = 1;

console.log(flat(array, n));
