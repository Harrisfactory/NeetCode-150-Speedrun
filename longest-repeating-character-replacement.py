class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        #create a hashmap and store all unique chars and there count

        #sliding window approach where if majority in window minus window len <= k our window is valid and we can expand, otherwise we shift left pointer until it is valid

        frequent_chars = {}

        l, r = 0, 0

        longest = 0

        while r < len(s):
            #update dictionary
            if s[r] in frequent_chars:
                frequent_chars[s[r]]+=1
            else:
                frequent_chars[s[r]] = 1

            #check if window is valid
            while (r-l+1) - max(frequent_chars.values()) > k:
                #decrement s[l] from frequency
                frequent_chars[s[l]]-=1
                l+=1

            r+=1

            longest = max(longest, r-l)

        return longest     
