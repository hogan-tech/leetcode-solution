function jsonToMatrix(arr: any[]): (string | number | boolean | null)[][] {
    const isObject = (x: any): x is object =>
        x !== null && typeof x === "object";
    const getKeys = (arg: any): string[] => {
        if (!isObject(arg)) return [""];
        return Object.keys(arg).reduce((acc: string[], curr: string) => {
            return (
                acc.push(
                    ...getKeys(arg[curr]).map((x: string) =>
                        x ? `${curr}.${x}` : curr
                    )
                ),
                acc
            );
        }, []);
    };

    const keys: string[] = [
        ...arr.reduce((acc: Set<string>, curr: any) => {
            getKeys(curr).forEach((k: string) => acc.add(k));
            return acc;
        }, new Set<string>()),
    ].sort();

    const getValue = (
        obj: any,
        path: string
    ): string | number | boolean | null => {
        const paths: string[] = path.split(".");
        let i = 0;
        let value: any = obj;
        while (i < paths.length) {
            if (!isObject(value)) break;
            value = value[paths[i++]];
        }
        if (i < paths.length || isObject(value) || value === undefined)
            return "";
        return value;
    };

    const matrix: (string | number | boolean | null)[][] = [keys];
    arr.forEach((obj: any) => {
        matrix.push(keys.map((key: string) => getValue(obj, key)));
    });
    return matrix;
}

const arr2 = [
    { b: 1, a: 2 },
    { b: 3, a: 4 },
];

console.log(jsonToMatrix(arr2));
