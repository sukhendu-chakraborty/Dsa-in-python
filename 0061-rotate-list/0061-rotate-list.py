# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        length = 1
        curr = head
        while curr.next:
            length += 1
            curr = curr.next
        k = k % length
        if k == 0:
            return head
        l = head
        for i in range(length-k-1):
            l = l.next
        curr.next=head
        head = l.next
        l.next = None


        return head


        