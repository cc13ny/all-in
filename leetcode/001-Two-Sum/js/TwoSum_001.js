/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    var num, i = 0, map = {};
    for (num of nums) {
        if (target - num in map) {
            return [map[target - num] + 1, i + 1];
        }
        map[num] = i;
        i++;
    }
};
