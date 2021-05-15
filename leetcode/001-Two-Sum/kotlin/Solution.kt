class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        var numIdx: HashMap<Int, Int> = HashMap<Int, Int>()
        nums.forEachIndexed { i, num ->
            if (numIdx.containsKey(target - num)) {
                return intArrayOf(numIdx.getValue(target - num), i)
            }
            numIdx.put(num, i)
        }
        return intArrayOf()
    }
}