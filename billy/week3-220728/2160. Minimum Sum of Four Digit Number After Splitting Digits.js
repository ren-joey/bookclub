/**
 * @param {number} num
 * @return {number}
 */
var minimumSum = function(num) {
    let val = 2568;
    let sum = 0;

    while (val) {
        sum += val % 10;
        val = Math.floor(val / 10);
    }

    return sum;
};