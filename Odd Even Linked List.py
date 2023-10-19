class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        o,e,heade = head, head.next,head.next        
        while e and e.next:
            o.next = o.next.next
            e.next = e.next.next
            o = o.next
            e = e.next  
        o.next = heade
        return head        
        
