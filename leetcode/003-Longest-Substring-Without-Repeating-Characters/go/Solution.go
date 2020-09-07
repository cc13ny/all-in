func lengthOfLongestSubstring(s string) int {
	res, leftmost := 0, 0

	var chars [255]int
	for i, _ := range chars {
		chars[i] = -1
	}

	for i, c := range s {
	    leftmost = max(leftmost, chars[int(c)]+1)
		res = max(res, i - leftmost + 1)
		chars[int(c)] = i
	}

	return res
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}