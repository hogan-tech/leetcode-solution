function cancellable<T>(generator: Generator<Promise<any>, T, unknown>): [() => void, Promise<T>] {
    let reject = null, resolve = null;

    let n, value;
    let promise = new Promise<T>(async (res,rej) => {
        reject = rej;
        resolve = res;
        try {
            for (n = generator.next(); !n.done; n = generator.next(value)) {
                value = await n.value;
            }

            res(n.value);

        } catch(err) {
            await handleError(err);
        }
    });

    async function handleError(err) {
        try {
            console.log('in handle err');

            try {
                n = generator.throw(err);
            } catch(e) {
                reject(err);
                return;
            }

            value = await n.value;

            while(!n.done) {
                n = generator.next(value);
                value = await n.value;
                console.log(value, n.done);
            }
            value != void 0 ? resolve(value) : reject(err);
        } catch(e) {
            console.log(e, value);

            await handleError(err)
        }
    }

    const cancel = async () => {
        try {
            n = generator.throw(value);
            value = await n.value;
            resolve(value != void 0 ? value : "Cancelled");
        } catch(err) {
            reject("Cancelled");
        }

    }

    return [cancel, promise];
};

/**
 * function* tasks() {
 *   const val = yield new Promise(resolve => resolve(2 + 2));
 *   yield new Promise(resolve => setTimeout(resolve, 100));
 *   return val + 1;
 * }
 * const [cancel, promise] = cancellable(tasks());
 * setTimeout(cancel, 50);
 * promise.catch(console.log); // logs "Cancelled" at t=50ms
 */
