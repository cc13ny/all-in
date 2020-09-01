class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var numIdx = [Int: Int]()
        for (i, num) in nums.enumerated() {
            if numIdx[target - num] != nil {
                return [numIdx[target - num]!, i]
            }
            numIdx[num] = i
        }
        return []
    }
}