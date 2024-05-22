class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        triplets = set()

        nums = sorted(nums)

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1

            while l < r:
                num_sum = nums[i] + nums[l] + nums[r]
                if num_sum == 0:
                    triplets.add(tuple([nums[i], nums[l], nums[r]]))
                    l+=1
                    r-=1
                elif num_sum > 0:
                    r-=1
                elif num_sum < 0:
                    l+=1
                else:
                    l+=1
                    r-=1