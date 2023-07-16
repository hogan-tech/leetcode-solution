/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function (object) {
  switch (typeof object) {
    case "object":
      if (Array.isArray(object)) {
        const elements = object.map((element) => jsonStringify(element));
        return `[${elements.join(",")}]`;
      } else if (object) {
        const keys = Object.keys(object);
        const keyValuePairs = keys.map(
          (key) => `"${key}":${jsonStringify(object[key])}`
        );
        return `{${keyValuePairs.join(",")}}`;
      } else {
        return "null";
      }
    case "boolean":
    case "number":
      return `${object}`;
    case "string":
      return `"${object}"`;
    default:
      return "";
  }
};