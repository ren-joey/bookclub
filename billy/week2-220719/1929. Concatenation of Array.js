/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    let list = [];

    for (i = 0; i < nums.length * 2; i += 1) {
        list.push(nums[i >= nums.length ? i - nums.length : i]);
    }

    return list;
};