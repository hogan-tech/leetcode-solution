function jsonStringify(object: any): string {
    switch (typeof object) {
        case "object":
            if (Array.isArray(object)) {
                const elements = object.map((element) =>
                    jsonStringify(element)
                );
                return `[${elements.join(",")}]`;
            } else if (object) {
                const keys = Object.keys(object);
                const keyValuePairs = keys.map((key) => {
                    return `"${key}":${jsonStringify(object[key])}`;
                });
                return `{${keyValuePairs.join(",")}}`;
            } else {
                return "null";
            }
            return object;
        case "boolean":
        case "number":
            return `${object}`;
        case "string":
            return `"${object}"`;
        default:
            return "";
    }
}
