package _go

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	p := new(ListNode)
	dump := p
	l1_val, l2_val, c, sum := 0, 0, 0, 0

	for l1 != nil || l2 != nil {
		if l1 != nil {
			l1_val = l1.Val
			l1 = l1.Next
		}

		if l2 != nil {
			l2_val = l2.Val
			l2 = l2.Next
		}

		sum = l1_val + l2_val + c
		p.Next = new(ListNode)
		p = p.Next
		p.Val, c = sum % 10, sum / 10

		l1_val, l2_val = 0, 0
	}

	if c == 1 {
		p.Next = &ListNode{1, nil}
	}

	return dump.Next
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}