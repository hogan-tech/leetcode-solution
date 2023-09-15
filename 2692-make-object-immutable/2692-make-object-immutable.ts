type Obj = Array<any> | Record<string, any>;

const makeImmutable = (obj: Obj): Obj => {
    // Define the methods that we want to block on our immutable object
    const methods = new Set(['pop', 'push', 'shift', 'unshift', 'splice', 'sort', 'reverse']);

    // Depth-first search function to traverse and handle different types of elements in the object
    function dfs(obj: Obj): Obj {
        // If the object is null, we just return it directly
        if(obj === null) return null;

        // Handle function types separately to block mutating methods
        if(typeof obj === 'function') {
            return new Proxy(obj, {
                apply(func: Function, thisArg: any, argumentList: any[]) {
                    // Block the execution of certain methods
                    if(methods.has(func.name)) {
                        throw `Error Calling Method: ${func.name}`;
                    }
                    return func.apply(thisArg, argumentList);
                }
            });
        }

        // Handle array types
        if(Array.isArray(obj)) {
            return  new Proxy(obj, {
                set(_: Obj, prop: string | number | symbol) {
                    // Block the modification of the array
                    throw `Error Modifying Index: ${prop.toString()}`;
                },
                get(obj: Obj, prop: string | number | symbol) {
                    // Continue the depth-first search for each element in the array
                    return dfs(obj[prop as keyof typeof obj]);
                }
            });
        }

        // If it's not an object, we don't need to do anything special with it, so we return it directly
        if(typeof obj !== 'object') return obj;

        // Handle object types
        return new Proxy(obj, {
            set(_: Obj, prop: string | number | symbol) {
                // Block the modification of the object
                throw `Error Modifying: ${prop.toString()}`;
            },
            get(obj: Obj, prop: string | number | symbol) {
                // Continue the depth-first search for each property of the object
                return dfs(obj[prop as keyof typeof obj]);
            }
        });
    }

    // Start the depth-first search on the initial object
    return dfs(obj);
};
