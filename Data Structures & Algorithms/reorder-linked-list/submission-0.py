class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        curr = slow.next
        slow.next = None
        
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        l1 = head
        l2 = prev

        while l2:
            tmp1 = l1.next
            tmp2 = l2.next
            
            l1.next = l2
            l2.next = tmp1
            
            l1 = tmp1
            l2 = tmp2
            
        return None