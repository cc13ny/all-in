object Solution {
  def twoSum(nums: Array[Int], target: Int): Array[Int] = {
    var numIdx: Map[Int, Int] = Map()
    for((num, i) <- nums.view.zipWithIndex) {
      if (numIdx.contains(target - num)) {
        return Array(numIdx.get(target - num).getOrElse(-1), i)
      }
      numIdx += (num -> i)
    }
    return Array[Int]()
  }
}