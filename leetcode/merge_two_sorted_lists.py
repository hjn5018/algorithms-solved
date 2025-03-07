# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1_ = []
        while list1:
            list1_.append(list1.val)
            list1 = list1.next
        list2_ = []
        while list2:
            list2_.append(list2.val)
            list2 = list2.next
        # print(list1_)
        # print(list2_)
        result = list1_ + list2_
        result.sort()
        # print(result)
        if result:
            next_ = ListNode(result.pop(), None)
            while result:
                next_ = ListNode(result.pop(), next_)
            # print(next_)
            return next_

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1

# https://leetcode.com/problems/merge-two-sorted-lists/submissions/1476920073/?envType=problem-list-v2&envId=linked-list
