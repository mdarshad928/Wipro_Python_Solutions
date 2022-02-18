def caseCount(string):
  UCcount = 0
  LCcount = 0
  for i in string:
    if i.isupper():
      UCcount += 1
    
    elif i.islower():
      LCcount += 1
  print("Upper Case Count = ", UCcount, "Lower Case Count = ", LCcount)

if __name__ == "__main__":
  string = input("Enter your string: ")
  caseCount(string)