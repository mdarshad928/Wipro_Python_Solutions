string = input("Enter a String: ")
length = len(string)
if string[0]== "x" and string[-1]=="x":
  print(string[1:length-1])
elif string[0] == "x":
  print(string[1: length])
elif string[-1] == "x":
  print(string[0: length-1])
else:
  print(string)