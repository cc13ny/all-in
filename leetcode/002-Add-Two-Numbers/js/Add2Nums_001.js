/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
    var dumpy = new ListNode(0);
    var p = dumpy;
    var c = 0;

    while (l1 && l2) {
        p.next = new ListNode((c + l1.val + l2.val) % 10);
        c = Math.floor((c + l1.val + l2.val) / 10);
        p = p.next;
        l1 = l1.next;
        l2 = l2.next;
    }

    while (l1) {
        p.next = new ListNode((c + l1.val) % 10);
        c = Math.floor((c + l1.val) / 10);
        p = p.next;
        l1 = l1.next;
    }

    while (l2) {
        p.next = new ListNode((c + l2.val) % 10);
        c = Math.floor((c + l2.val) / 10);
        p = p.next;
        l2 = l2.next;
    }

    if (c) {
        p.next = new ListNode(1);
    }

    return dumpy.next;
};