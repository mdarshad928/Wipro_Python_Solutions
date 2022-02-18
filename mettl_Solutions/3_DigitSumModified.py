"""Given an input find the digit sum. Do this untill digit sum is one digit number.

Example:
input = 9941
first iteration = (9+9+4+1= 23)  is less greater than 9.
second iteration = (2+3 = 5) is less than 10 hence output is 5"""


def digit_sum_modified(input1: int)->int:
  #Pastable Code starts from here
  inp = abs(input1)
  while inp > 9:
    sumVal = 0
    while inp>0:
      sumVal += inp%10
      inp //= 10
    inp = sumVal  
  if input1<0:
    return -inp
  else:
    return inp
  #Pastable Code ends here

if __name__ == "__main__":
  input1 = int(input("Enter a number: "))
  print(digit_sum_modified(input1))