def sumInd(num, x, y):
  ans = 0
  target = num[x] + num[y]
  print('Target: ',target)

  # while(target!=0):
  #   ans = ans+(target%10)
  #   target = target//10
  # print(ans)

  ans = x+y
  return(ans)

num = [2.5, 7.5, 11.2, 15.1]
answer = sumInd(num, 0,1)
print('Answer: ',answer)