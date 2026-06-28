class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        new=[]
        for i in nums[:]: #nums[:] -> Creates a copy of orginal list (nums). The copy of original list does not change while looping, only orginal list (nums) will change.
            if i == 0:
                new.append(i)
                nums.remove(i)
        nums.extend(new)   #used for extending one list with another list
        print(nums)

                
        
