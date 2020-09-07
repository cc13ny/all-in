/**
 * Definition for singly-linked list.
 * class ListNode(_x: Int = 0, _next: ListNode = null) {
 *   var next: ListNode = _next
 *   var x: Int = _x
 * }
 */
object Solution {
  def addTwoNumbers(l1: ListNode, l2: ListNode): ListNode = {
    val dump = new ListNode
    var sum, c, l1_val, l2_val:Int = 0
    var (p, pl1, pl2) = (dump, l1, l2)

    while(pl1 != null || pl2 != null) {
      if (pl1 != null) {
        l1_val = pl1.x
        pl1 = pl1.next
      }

      if (pl2 != null) {
        l2_val = pl2.x
        pl2 = pl2.next
      }

      sum = c + l1_val + l2_val
      p.next = new ListNode(sum % 10)
      p = p.next
      c = sum / 10

      l1_val = 0; l2_val = 0
    }

    if (c == 1) {
      p.next = new ListNode(1)
    }

    return dump.next
  }
}