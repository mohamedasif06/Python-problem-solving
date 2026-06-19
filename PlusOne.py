def plusOne(digits):
      for i in range(len(digits)-1,-1,-1):
          if digits[i]<9:
              digits[i] += 1
              return digits
          digits[i]=0
      else:
          return [1]+digits
digits = list(map(int,input("Enter integers for array: ").split()))
print(plusOne(digits))
