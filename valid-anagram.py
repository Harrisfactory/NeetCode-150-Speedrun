class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        t_dict = {}
        s_dict = {}

        for letter in t:
            if letter in t_dict:
                t_dict[letter]+=1
            else:
                t_dict[letter] = 1
        
        for letter in s:
            if letter in s_dict:
                s_dict[letter]+=1
            else:
                s_dict[letter] = 1
        
        if t_dict == s_dict:
            return True
        return False