"""Given a list add 1 if the list content is odd and 2 if the list content is even

Example:
input : [1, 4, 8, 3]
output : [2, 6, 10, 4]"""

def list_manipulate(input1: list)->list:
  # Pastable Code starts from here
  newList = []
  for i in input1:
    if i%2 == 0:
      newList.append(i+2)
    else:
      newList.append(i+1)
  return newList
  # Pastable Code ends here

if __name__ == "__main__":
  input1 = list(map(int, input("Enter list contents separated by space: ").split()))
  print("Output is =", list_manipulate(input1))
