package _go

func longestPalindrome(s string) string {
	// otherwise the index will be out of the bound for ""
	if s == "" {
		return ""
	}

	var max_len, possible_max_len int
	var res_idx, tmp_idx, tmp1_idx, tmp2_idx [2]int

	for i, _ := range s {
		possible_max_len = 2*min(i, len(s)-1-i) + 2
		if possible_max_len > max_len {
			tmp1_idx = get_max_len_idx(i, i, s)
			tmp2_idx = get_max_len_idx(i+1, i, s)
			if tmp1_idx[1]-tmp1_idx[0] > tmp2_idx[1]-tmp2_idx[0] {
				tmp_idx = tmp1_idx
			} else {
				tmp_idx = tmp2_idx
			}

			if tmp_idx[1]-tmp_idx[0]+1 > max_len {
				max_len = tmp_idx[1] - tmp_idx[0] + 1
				res_idx = tmp_idx
			}
		}
	}

	return s[res_idx[0] : res_idx[1]+1]
}

func min(x, y int) int {
	if x > y {
		return y
	}
	return x
}

func get_max_len_idx(i int, j int, s string) [2]int {
	l, r := i, j
	for 0 <= l-1 && r+1 < len(s) && s[l-1] == s[r+1] {
		l -= 1
		r += 1
	}

	return [2]int{l, r}
}
