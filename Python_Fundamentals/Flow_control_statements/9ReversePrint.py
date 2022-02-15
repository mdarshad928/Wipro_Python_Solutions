num = int(input("Enter a Number: "))      #1234
power = len(str(num))
revNum = 0

while num>0:
  revNum += (num%10)*10**(power-1)
  power -= 1
  num = num//10

print(revNum)