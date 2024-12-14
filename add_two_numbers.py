# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverseNumber(head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            while head:
                next_node = head.next
                head.next = prev
                prev = head
                head = next_node
            return prev
        def toInt(head: Optional[ListNode]) -> int:
            head = reverseNumber(head)
            list_ = []
            while head:
                list_.append(head.val)
                head = head.next
            int_ = int(''.join(map(str, list_)))
            return int_
        num_ = toInt(l1) + toInt(l2)
        list_ = list(map(int, str(num_)))[::-1]
        result = ListNode(list_.pop(), None)
        while list_:
            result = ListNode(list_.pop(), result)
        return result
# https://leetcode.com/problems/add-two-numbers/description/
