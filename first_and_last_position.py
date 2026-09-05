# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
       return [self.first(nums,target),self.last(nums,target)]

    def first(self,nums,target):
        l=0
        r = len(nums)-1
        ans=-1 # -1 means target has not been found yet
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                ans = mid
                r = mid-1

          # Middle value is smaller than target # So target must be on the RIGHT
            elif nums[mid]<target:
                l=mid+1
          # Middle value is greater than target # So target must be on the LEFT
            else:
                r=mid-1
        return ans

    def last(self,nums,target):
        l=0
        r = len(nums)-1
        ans=-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                ans = mid
                l=mid+1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return ans

        

