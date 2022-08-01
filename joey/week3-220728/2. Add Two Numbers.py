"""
Runtime: 71 ms, faster than 91.72% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.8 MB, less than 86.72% of Python3 online submissions for Add Two Numbers.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head

        while(l1 is not None):
            tail.val = l1.val
            if (l1.next is not None):
                tail.next = ListNode()
            tail = tail.next
            l1 = l1.next

        tail = head
        l2Tail = l2
        overflow = 0
        while(l2Tail is not None or overflow != 0):
            if (l2Tail is not None):
                tail.val = tail.val + l2Tail.val + overflow
                l2Tail = l2Tail.next
            else:
                tail.val = tail.val + overflow
            overflow = 0

            while (tail.val > 9):
                tail.val -= 10
                overflow += 1

            if (tail.next is None
                    and (overflow != 0 or l2Tail is not None)):
                tail.next = ListNode()
            tail = tail.next

        return head

class Solution2:
    def addTwoNumbers(self, l1, l2):
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0
        def tolist(n):
            node = ListNode(n % 10)
            if n > 9:
                node.next = tolist(n / 10)
            return node
        return tolist(toint(l1) + toint(l2))