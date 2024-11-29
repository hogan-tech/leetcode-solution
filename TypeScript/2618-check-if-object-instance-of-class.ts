function checkIfInstanceOf(obj: any, classFunction: any): boolean {
    if (
        obj === null ||
        obj === undefined ||
        typeof classFunction !== "function"
    )
        return false;

    let currentPrototype = Object.getPrototypeOf(obj);

    while (currentPrototype !== null) {
        if (currentPrototype === (classFunction as Function).prototype)
            return true;
        currentPrototype = Object.getPrototypeOf(currentPrototype);
    }

    return false;
}

console.log(checkIfInstanceOf(new Date(), Date));

class Animal {}
class Dog extends Animal {}
console.log(checkIfInstanceOf(new Dog(), Animal));

console.log(checkIfInstanceOf(Date, Date));
