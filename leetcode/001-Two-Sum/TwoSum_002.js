/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var num_idx_pairs = [];
    var i;
    for (i = 0; i < nums.length; i++) {
        num_idx_pairs.push([nums[i], i + 1]);
    }
    num_idx_pairs.sort(function(a, b){return a[0] > b[0]});
    console.log(num_idx_pairs);
    
    var l = 0, r = nums.length - 1;
    var lpr, rpr, sum;
    while (l < r) {
        lpr = num_idx_pairs[l];
        rpr = num_idx_pairs[r];
        sum = lpr[0] + rpr[0];
        if (sum < target) {
            l++;
        } else if (sum > target) {
            r--;
        } else {
            var id1 = lpr[1], id2 = rpr[1];
            return id1 < id2 ? [id1, id2] :[id2, id1];
        }
    }
};