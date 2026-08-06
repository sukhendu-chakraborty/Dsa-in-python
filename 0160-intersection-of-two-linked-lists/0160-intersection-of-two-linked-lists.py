# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def length(self,head):
        l = 0
        curr = head
        while curr.next:
            l += 1
            curr = curr.next
        return l
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA==headB:
                return headA
        lenA= self.length(headA)
        lenB= self.length(headB)
        if lenA>lenB:
            d = lenA-lenB
            for i in range(d):
                headA= headA.next
        else:
            d = lenB-lenA
            for i in range(d):
                headB= headB.next
        for i in range(max(lenA,lenB)):
            if headA==headB:
                return headA
            else:
                headA=headA.next
                headB=headB.next
        return None
            
        

        