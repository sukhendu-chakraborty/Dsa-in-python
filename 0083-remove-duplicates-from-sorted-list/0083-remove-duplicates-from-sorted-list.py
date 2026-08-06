# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        s = head
        f = s.next
        while f!=None:
            if s.val == f.val:
                f = f.next
                s.next = f
            else:
                f =f.next
                s= s.next
        return head
        
            



        