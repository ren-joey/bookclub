/**
 * @param {string} s
 * @param {number[]} indices
 * @return {string}
 */
var restoreString = function(s, indices) {
    let ansList = new Array(s.length);

    for (let i = 0; i < s.length; i += 1) ansList[indices[i]] = s[i];

    return ansList.join('');
};