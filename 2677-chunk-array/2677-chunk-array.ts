function chunk(arr: any[], size: number): any[][] {
    let result: number[][] = [];
    let index = 0;
    while (index < arr.length) {
        let count = size;
        let row: number[] = [];
        while (count-- > 0 && index < arr.length) {
            row.push(arr[index]);
            index++;
        }
        result.push(row);
    }

    return result;
}

const arr1 = [1, 2, 3, 4, 5],
    size1 = 2;
console.log(chunk(arr1, size1));
