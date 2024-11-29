function twoSum(nums: number[], target: number): number[] {
  const numMap: { [key: number]: number } = {};
  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    const complement = target - num;
    if (complement in numMap) {
      return [numMap[complement], i];
    }
    numMap[num] = i;
  }
  return [];
}