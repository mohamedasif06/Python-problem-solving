class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[-3]*nums[-2]*nums[-1]  
        b = nums[0]*nums[1]*nums[-1]
        return max(a,b)

# There are only 2 possibilities for finding three numbers whose product is maximum and return the maximum product.
