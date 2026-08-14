# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stk =[]
        temp = head
        while temp:
            stk.append(temp.val)

            temp = temp.next
        temp = head    
        while stk:
            x = stk.pop()
            if temp.val != x:
                return False
            temp = temp.next    
        return True        
