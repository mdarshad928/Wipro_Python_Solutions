import sys
sum = 0
for i in range(1,len(sys.argv)):
  num = int(sys.argv[i])
  if num == 1:
    continue
  flag = 0
  for i in range(2,num):
    if (num%i) == 0:
      flag = 1

  if flag == 0:
    sum += num

print("Sum of prime arguments are : ", sum)
  
