def fact(num):
  result = 1
  for i in range(2, num+1):
    result *= i
  return result

if __name__ == "__main__":
  num = int(input("Enter a number to calculate the factorial: "))
  print(fact(num))