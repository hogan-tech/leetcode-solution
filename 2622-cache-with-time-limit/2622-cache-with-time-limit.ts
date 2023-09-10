type MapEntry = {
    value: number;
    timeout: NodeJS.Timeout;
};

class TimeLimitedCache {
    caches = new Map<number, MapEntry>();

    set(key: number, value: number, duration: number): boolean {
        const valueInCache = this.caches.get(key);
        if (valueInCache) {
            clearTimeout(valueInCache.timeout);
        }
        const timeout = setTimeout(() => this.caches.delete(key), duration);
        this.caches.set(key, { value, timeout });
        return Boolean(valueInCache);
    }

    get(key: number): number {
        const entry = this.caches.get(key);
        return entry?.value ?? -1;
    }

    count(): number {
        return this.caches.size;
    }
}

var obj = new TimeLimitedCache();
obj.set(1, 42, 1000); // false
console.log(obj.get(1)); // 42
console.log(obj.count()); // 1
