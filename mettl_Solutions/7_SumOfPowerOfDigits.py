def sumOfPowerOfDigits(input1: int):
  output = 0
  ld = 0
  while input1>0:
    output += pow(input1%10, ld)
    ld = input1 % 10
    output //= 10
  return output
if __name__ == "__main__":
  print(sumOfPowerOfDigits(582109))