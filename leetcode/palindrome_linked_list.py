# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dq = collections.deque()
        
        while head:
            dq.append(head.val)
            head = head.next

        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False
        return True
# https://leetcode.com/problems/palindrome-linked-list/
