/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function (fn) {
    let result = {}
    for(item of this){
        const key = fn(item)
        if(key in result){
            result[key].push(item)
        }else{
            result[key] = [item]
        }
    }
    return result
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */