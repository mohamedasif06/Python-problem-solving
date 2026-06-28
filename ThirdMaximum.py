class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))   #for removing duplicates
        nums.sort(reverse = True) #Sorting in descending order
        n = len(nums)
        if n>=3:
            return nums[2]
        else:
            return nums[0]


        
