/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    let res = 0;
    for (let i = 0; i < nums.length - 1; i += 1) {
        for (let j = i + 1; j < nums.length; j += 1) {
            if (nums[i] == nums[j]) {
                res++;
            }
        }
    }
    return res;
};