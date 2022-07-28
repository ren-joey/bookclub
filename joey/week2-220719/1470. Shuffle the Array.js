/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
 var shuffle = function(nums, n) {
    const arr = [];
    for (let i = 0; i < n; i += 1) {
        arr[i * 2] = nums[i];
    }

    for (let i = n; i < (2 * n); i += 1) {
        arr[(i - n + 1) * 2 - 1] = nums[i];
    }

    return arr;
};