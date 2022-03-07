def palind():
  num = int(input("Enter a number: "))        # 123456    , 1234, 123, 12, 1, 0
  
  l = len(str(num))-1
  numcopy = num                                  
  new = 0
  while numcopy>0:                                            # 6*100000 + 5*10000 + 4*1000 + 3*100 + 2*10 + 1
      new = new + (numcopy%10)*(10**l)
      l -= 1
      numcopy = numcopy//10
  
  if new == num:
      print("Yes")
  else:
      print("No")