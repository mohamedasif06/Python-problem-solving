def single_num(nums):
    ans = 0
    for i in nums:
        ans = ans^i   # XOR removes duplicates using binary
    return ans
nums = list(map(int,input("Enter numbers for array: ").split()))
result = single_num(nums)
print(f"The number occured once: {result}")
