# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        cnt=0
        while temp:
            cnt+=1
            temp=temp.next
        temp=head
        cnt-=n
        if(cnt==0):
            newhead=head.next
            return newhead
        temp=head
        while temp:
            cnt-=1
            if(cnt==0):
                break
            temp=temp.next
        temp.next=temp.next.next
        return head