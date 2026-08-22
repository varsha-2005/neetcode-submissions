# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        for i in range(left - 1):
            temp = temp.next
        prev = None
        curr = temp.next
        for i in range(right - left + 1):
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        temp.next.next = curr
        temp.next = prev
        return dummy.next