/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    arr1 = arr1.concat(arr2)
    const merge = {}
    for(item of arr1){
        const id = item.id
        if(merge[id]){
            merge[id] = {...merge[id],...item}
        }else{
            merge[id] = {...item}
        }

    }
    const resultArray = Object.values(merge)
    return resultArray
}