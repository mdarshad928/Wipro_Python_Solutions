"""Given two inputs (input1 of int type, input2 of str type) return the sum of digits. If input2 = odd give only odd digit sum and vice versa."""


def digit_sum_eo(input1: int, input2: str)->int:
  #Pastable Code Starts from here
  oddSum = 0
  sumVal = 0
  while input1>0:
      digit = input1%10
      sumVal += digit
      if (digit)%2 != 0:
          oddSum += digit
      input1 = input1//10
  if input2.lower() == "even":
      return (sumVal - oddSum)
  elif input2.lower() == "odd":
      return (oddSum)
  else:
      return ('write acceptable input2')
  #Pastable code ends here.

if __name__ == "__main__":
  input1 = int(input("Enter the Number: "))
  input2 = (input("Do you want Odd Digits Sum or Even Digits Sum?: "))
  print("Output: ", digit_sum_eo(input1, input2))