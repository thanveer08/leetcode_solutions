# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        count = 0
        if not head or not head.next:
            return None
        while temp:
            count +=1
            temp = temp.next
        if (count%2) != 0:
            
            dummy = ListNode()
            prev = dummy
            prev.next = head
            fast , slow = head, head
            while fast.next and fast.next.next :
                fast = fast.next.next
                slow = slow.next
                prev = prev.next
            prev.next = slow.next
            slow.next = None
        else:
            slow = fast = head
            while fast.next and fast.next.next :
                fast = fast.next.next
                slow = slow.next 
            dele = slow.next
            slow.next= slow.next.next  
            dele.next = None
        return head              