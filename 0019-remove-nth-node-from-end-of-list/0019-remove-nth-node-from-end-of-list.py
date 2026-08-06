# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s = head
        f = head
        for i in range(n):
            f = f.next
        if f == None:
            head=head.next
            return head
        while f.next!=None:
            f= f.next
            s= s.next
        s.next=s.next.next
        return head
        



        