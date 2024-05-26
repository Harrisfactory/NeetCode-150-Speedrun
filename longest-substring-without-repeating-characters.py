class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_window = set()
        ctr = 0
        l = 0
        r = 0
        longest = 0

        for i in range(len(s)):
            #check and move window if s[i] currently exists in the window, this is the sliding motion
            while s[i] in char_window:
                char_window.remove(s[l])
                l+=1 #move l over one before checking again
                ctr-=1
            char_window.add(s[i])
            ctr+=1
            longest = max(longest, ctr)
        
        return longest