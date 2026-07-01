# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
# A common string is a string that appeared in both list1 and list2.
# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
# Return all the common strings with the least index sum. Return the answer in any order.
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_index = float("inf") #-> This represents infinity
        res = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    curr_sum = i+j
                    if curr_sum < min_index:
                        min_index = curr_sum
                        res = [list1[i]]
                    elif curr_sum == min_index:
                        res.append(list1[i])
        return res
                    

