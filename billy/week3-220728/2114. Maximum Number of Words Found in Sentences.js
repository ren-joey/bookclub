/**
 * @param {string[]} sentences
 * @return {number}
 */
var mostWordsFound = function(sentences) {
    let max = [];
    let count = 0;

    for (let i = 0; i < sentences.length; i += 1) {
        for (let j = 0; j < sentences[i].length; j += 1) {
            if (sentences[i][j] === ' ') count++;
        }

        max.push(count);
        count = 0;
    }

    return Math.max(...max) + 1;
};