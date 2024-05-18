class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        frequencies = {}
        result = []

        for num in nums:
            if num in frequencies:
                frequencies[num]+=1
            else:
                frequencies[num] = 1
        
        while k > 0:
            max_val = 0
            max_key = 0
            for key, val in frequencies.items():
                if val > max_val:
                    max_key = key
                    max_val = val
            result.append(max_key)
            del frequencies[max_key]
            k-=1
        
        return result
    
    #O(n + k^f)