/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
 var shuffle = function(nums, n) {
    let list = [];

    for(let i = 0; i < n; i += 1){
        list.push(nums[i], nums[i + n]);
    }

    return list;
};