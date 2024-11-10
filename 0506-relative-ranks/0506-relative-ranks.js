/**
 * @param {number[]} score
 * @return {string[]}
 */
var findRelativeRanks = function (score) {
  const N = score.length;

  const heap = [];
  for (let index = 0; index < N; index++) {
    heap.push([score[index], index]);
  }

  heap.sort((a, b) => b[0] - a[0]);

  const rank = new Array(N);

  for (let place = 0; place < N; place++) {
    const originalIndex = heap[place][1];
    if (place === 0) {
      rank[originalIndex] = "Gold Medal";
    } else if (place === 1) {
      rank[originalIndex] = "Silver Medal";
    } else if (place === 2) {
      rank[originalIndex] = "Bronze Medal";
    } else {
      rank[originalIndex] = (place + 1).toString();
    }
  }

  return rank;
};
