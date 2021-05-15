object Solution {
  def lengthOfLongestSubstring(s: String): Int = {
    var left_most_idx, tmp_max_len, max_len: Int = 0
    var chars = Array.fill(255)(-1)

    for ((c, i) <- s.view.zipWithIndex) {
      if (chars(c.toInt) + 1 > left_most_idx) {
        left_most_idx = chars(c.toInt) + 1
      }
      tmp_max_len = i - left_most_idx + 1
      if (tmp_max_len > max_len) max_len = tmp_max_len
      chars(c.toInt) = i
    }
    return max_len
  }
}