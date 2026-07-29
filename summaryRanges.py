class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        n = len(nums)
        i=0

        while i < n:
            start = nums[i]
            while i < n-1 and nums[i]+1 == nums[i+1]:
                i+=1
            end = nums[i]
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}->{end}")
            i+=1
        return result
