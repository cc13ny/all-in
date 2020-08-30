/**
 * @param numbers: An array of Integer
 * @param target: target = numbers[index1] + numbers[index2]
 * @return: [index1 + 1, index2 + 1] (index1 < index2)
 */
const twoSum = function (numbers, target) {
    // write your code here
    const numbersIdx = {};
    for (let i = 0; i < numbers.length; i++) {
        const num = numbers[i]
        if((target - num) in numbersIdx) {
            return [numbersIdx[target - num], i]
        }
        numbersIdx[num] = i
    }
}