class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s)-1
        def palindrome(s,L,R):
            #base case:
            if L>=R:
                return True
            if not s[L].isalnum():
                return palindrome(s,L+1,R)
            if not s[R].isalnum():
                return palindrome(s,L,R-1)
            if s[L].lower()!=s[R].lower():
                return False
            return palindrome(s,L+1,R-1)            
        return palindrome(s,L,R)