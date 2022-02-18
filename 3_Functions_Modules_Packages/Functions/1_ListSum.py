def ListSum(alist):
  sum = 0
  for i in alist:
    sum += i
  return sum

if __name__=="__main__":
  alist = [1, 2, 3, 4, 5, 7]
  print("Sample List = ", alist)
  alist = ListSum(alist)
  print("Sum of List Elements is = ", alist)