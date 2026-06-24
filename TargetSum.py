l = [1,2,3,4,5]
target = 6
found = False
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j] == target:
            print(f"The Pairs found at index {i} and {j}.\nThe Elements are {l[i]} and {l[j]}.")
            found = True
if found == False:
    print("No pairs attained the Target.")
            
            
