string = input("Enter your string: ")

UCcount = 0
LCcount = 0
for i in string:
  if i.isupper():
    UCcount += 1
  
  elif i.islower():
    LCcount += 1
  
print("Upper Case Count = ", UCcount, "Lower Case Count = ", LCcount)