function checkIfInstanceOf(obj: any, classFunction: any): boolean {
    if (
        obj === null ||
        obj === undefined ||
        typeof classFunction !== "function"
    )
        return false;

    let currPotentialPrototype = Object.getPrototypeOf(obj);

    while (currPotentialPrototype !== null) {
        if (currPotentialPrototype === (classFunction as Function).prototype)
            return true;
        currPotentialPrototype = Object.getPrototypeOf(currPotentialPrototype);
    }

    return false;
}

console.log(checkIfInstanceOf(new Date(), Date));

class Animal {}
class Dog extends Animal {}
console.log(checkIfInstanceOf(new Dog(), Animal));

console.log(checkIfInstanceOf(Date, Date));