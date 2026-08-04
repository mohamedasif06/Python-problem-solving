class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        large = max(nums)
        small = min(nums)
        new = set(nums) #converting to set because python takes only O(1) time for checking elements in set.
        missing = []
        for i in range(small,large+1): #using large+1 because the stop value is not included in for loop. So that it goes until it reaches the large.
            if i not in new:
                missing.append(i)
        return missing

