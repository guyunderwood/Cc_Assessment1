def sumInd(num, target, diff):
  for i in range(len(num)):
    for j in range(i+1, len(num)):
      sum = num[i]+num[j]
      if (sum == target):
        if (diff==1):
          ans = abs(i-j)
        else:
          ans = i+j
        return (ans)


num = [2.5, 7.5, 11.2, 15.1]
answer = sumInd(num, 22.6,1)
print('Answer: ',answer)