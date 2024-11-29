type F1 = (...args: any[]) => void;

function throttle(fn: F1, t: number): F1 {
    let timer: any;
    let nextTimeToCall = 0;
    return function (...args) {
        let delay = Math.max(0, nextTimeToCall - Date.now());
        clearTimeout(timer);
        timer = setTimeout(() => {
            fn(...args);
            nextTimeToCall = Date.now() + t;
        }, delay);
    };
}

const throttled = throttle(console.log, 100);
throttled("log"); // logged immediately.
throttled("log"); // logged at t=100ms.
