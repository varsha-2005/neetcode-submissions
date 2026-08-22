class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        temp = second
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        first = head
        second = prev
        while second:
            front1 = first.next
            front2 = second.next
            first.next = second
            second.next = front1
            first = front1
            second = front2