"""Write a function which returns nth fibonacci number.
Here fibonacci number is: 0, 1, 1, 2, 3, 5, 8, 13 and so on"""


def fibo(input1: int)-> int:
  #Pastable Code starts from here
  a = 0
  b = 1
  if input1 == 1:
    return a
  count = 2
  while count<input1:
    a, b = b, a+b
    count += 1

  return b
  #Pastable Code ends here


if __name__ == "__main__":
  input1 = int(input("Enter a Nth term you want: "))
  print(f'{input1}th fibonacci term is: ',fibo(input1))