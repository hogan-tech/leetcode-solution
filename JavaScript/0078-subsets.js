var subsets = function (nums) {
	let output = [[]];
	for (let num of nums) {
		let newSubsets = [];
		for (let curr of output) {
			let temp = curr.slice();
			temp.push(num);
			newSubsets.push(temp);
		}
		for (let curr of newSubsets) {
			output.push(curr);
		}
	}
	return output;
};