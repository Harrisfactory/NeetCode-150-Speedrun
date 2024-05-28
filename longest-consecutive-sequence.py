class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #convert nums to set 
        #if left of cur num is not in set
            #inc length of cur sequence until right neighbor not in set
        #then update longest

        numSet = set(nums)

        longest = 0

        for number in nums:
            if number - 1 not in numSet: #no left neighbor, start of sequence
                seq_len = 1
                while number + seq_len in numSet: #keep moving cur number by growing length until we cant find neighbor
                    seq_len+=1
                longest = max(seq_len, longest)
        
        return longest