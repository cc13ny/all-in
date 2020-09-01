# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    num_idx = {}
    nums.each_with_index do |num, i|
        if num_idx[target - num]
            return [num_idx[target - num], i]
        end
        num_idx[num] = i
    end
end