declare global {
    interface Array<T> {
        groupBy(fn: (item: T) => string): Record<string, T[]>
    }
}

Array.prototype.groupBy = function <T>(fn: (item: T) => string) {
    return this.reduce((accum, item) => {
        const key = fn(item);
        accum[key] ||= [];
        accum[key].push(item);
        return accum;
    }, {} as Record<string, T[]>);
};

[1, 2, 3].groupBy(String); // {"1":[1],"2":[2],"3":[3]}
