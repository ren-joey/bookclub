/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let list = [];

    for(let i = 0; i < nums.length; i += 1) {
        if (i !== 0) list.push(list[i - 1] + nums[i]);
        else list.push(nums[i]);
    }

    return list;
};