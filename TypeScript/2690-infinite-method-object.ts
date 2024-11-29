function createInfiniteObject(): Record<string, () => string> {
    return new Proxy(
        {},
        {
            get: (_, props) => () => props,
        }
    );
}

const obj2 = createInfiniteObject();
obj2["abc123"](); // "abc123"
