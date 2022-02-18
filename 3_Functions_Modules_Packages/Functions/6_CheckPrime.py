num = int(input("Enter a Number: "))
def checkPrime(num):
  flag = 0
  for i in range(2,num):
    if (num%i) == 0:
      flag = 1

  if flag == 1:
    print("No it is not a Prime Number")
  else:
    print("Yes it is a prime number")

checkPrime(num)