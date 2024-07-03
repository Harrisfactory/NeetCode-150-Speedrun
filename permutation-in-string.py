class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        window_l: int = 0
        window_r: int = len(s1)

        sorted_s1: str = sorted(s1)

        while window_r < len(s2):
            if sorted(s2[window_l:window_r]) == sorted_s1:
                return True
            window_l+=1
            window_r+=1
        
        if sorted(s2[window_l:window_r]) == sorted_s1:
                return True

        return False