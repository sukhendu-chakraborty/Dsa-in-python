# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cycle = False
        if not head:
            return None
        s = head
        f = head
        while f!=None and f.next!=None:
            s = s.next
            f = f.next.next
            if s==f:
                cycle = True
                break
        if not cycle:    
            return None
        if cycle:
            l = 1
            while s.next!=f:
                s = s.next
                l+=1
                
            s = head
            f = head
            for i in range(l):
                f=f.next
            while s!=f:
                s = s.next
                f = f.next
            return s
                
        
        
            


        
        