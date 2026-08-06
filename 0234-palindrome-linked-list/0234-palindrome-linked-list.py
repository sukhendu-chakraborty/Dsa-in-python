class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
            
        return values == values[::-1]
