class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #two pointer approach because we want to check left and right

        #[] compare only alphanumeric characters

        l, r = 0, len(s) - 1

        s = s.lower()

        while l < r:
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                return False
        return True