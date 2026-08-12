# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        temp = head

        if not temp:
            return None
        
        front = temp.next
        while front is not None:
            temp.next = prev
            prev = temp
            temp = front
            front = front.next
        temp.next = prev    
        return temp    