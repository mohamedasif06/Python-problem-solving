class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        i=0
        while i<n:
            if arr[i]==0:
                arr.insert(i+1,0)
                arr.pop()
                i = i+2
            else:
                i+=1
        print(arr)

        
