var searchMatrix = function (matrix, target) {
	if (matrix.length === 0) return false;
	const rows = matrix.length;
	const cols = matrix[0].length;
	let left = 0;
	let right = rows * cols - 1;
	while (left <= right) {
		const mid = Math.floor(left + (right - left) / 2);
		const value = matrix[Math.floor(mid / cols)][mid % cols];
		if (value < target)
			left = mid + 1;
		else if (value > target)
			right = mid - 1;
		else
			return true;
	}
	return false;
};