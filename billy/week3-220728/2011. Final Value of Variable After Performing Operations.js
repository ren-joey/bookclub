/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function(operations) {
    let result = 0;

    for (let i = 0; i < operations.length; i += 1) {
        const operation = operations[i];

        if (operation === 'X++' || operation === '++X') {
            result += 1;
        } else if (operation === 'X--' || operation === '--X') {
            result -= 1;
        }
    }

    return result;
};