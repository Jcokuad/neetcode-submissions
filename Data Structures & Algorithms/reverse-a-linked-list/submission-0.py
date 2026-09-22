# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr: # while curr is assigned to a node
            nxt = curr.next
            curr.next = prev # reverse the link
            prev = curr # iterate to the next node
            curr = nxt
        return prev