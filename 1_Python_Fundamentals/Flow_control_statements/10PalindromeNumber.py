num = int(input("Enter a Number: "))
numcache = num
power = len(str(num))
revNum = 0

while num>0:
  revNum += (num%10)*10**(power-1)
  power -= 1
  num = num//10

if numcache == revNum:
  print("It is a Palindrome Number")
else:
  print("It is not a Palindrome Number")