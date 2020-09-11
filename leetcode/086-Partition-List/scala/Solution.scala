/**
 * Definition for singly-linked list.
 * class ListNode(_x: Int = 0, _next: ListNode = null) {
 *   var next: ListNode = _next
 *   var x: Int = _x
 * }
 */
object Solution {
  def partition(head: ListNode, x: Int): ListNode = {
    var smaller = new ListNode
    var bigger = new ListNode

    val shead = smaller
    val bhead = bigger

    var p = head

    while(p != null) {
      if (p.x < x) {
        smaller.next = ListNode(p.x)
        smaller = smaller.next
      } else {
        bigger.next = ListNode(p.x)
        bigger = bigger.next
      }
      p = p.next
    }

    if (shead.next != null) {
      smaller.next = bhead.next
      return shead.next
    }

    return bhead.next
  }
}