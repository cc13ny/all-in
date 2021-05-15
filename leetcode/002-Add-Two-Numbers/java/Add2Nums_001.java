/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode(int x) {
 * val = x;
 * next = null;
 * }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int a;
        int b;
        int c = 0;
        int sum;

        ListNode l3 = new ListNode(c);

        ListNode p1 = l1;
        ListNode p2 = l2;
        ListNode p3 = l3;

        while (true) {
            a = p1.val;
            b = p2.val;

            sum = a + b + c;

            if (sum > 9) {
                p3.val = sum - 10;
                c = 1;
            } else {
                p3.val = sum;
                c = 0;
            }

            p1 = p1.next;
            p2 = p2.next;

            if ((p1 == null) || (p2 == null)) {
                break;
            }

            p3.next = new ListNode(0);
            p3 = p3.next;
        }

        if (p1 != null) {
            while (p1 != null) {
                a = p1.val;
                sum = a + c;

                if (sum > 9) {
                    c = 1;
                    p3.next = new ListNode(sum - 10);
                } else {
                    c = 0;
                    p3.next = new ListNode(sum);
                }

                p3 = p3.next;
                p1 = p1.next;
            }

        } else if (p2 != null) {
            while (p2 != null) {
                b = p2.val;
                sum = b + c;

                if (sum > 9) {
                    c = 1;
                    p3.next = new ListNode(sum - 10);
                } else {
                    c = 0;
                    p3.next = new ListNode(sum);
                }

                p3 = p3.next;
                p2 = p2.next;
            }
        }

        if (c == 1) {
            p3.next = new ListNode(1);
        }

        return l3;

    }
}
