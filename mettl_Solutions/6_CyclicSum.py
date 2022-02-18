def cyclic_sum(input1: int)->int:
  # Pastable Code starts from here
  string = str(input1)
  cyStringInd = 0
  sumVal = 0
  while cyStringInd<len(string):
      cyString = string[cyStringInd:len(string)]
      for i in cyString:
          sumVal += int(i)
      cyStringInd += 1

  return sumVal
  # Pastable Code ends here

if __name__ == "__main__":
  input1 = int(input("Enter a number: "))
  print(cyclic_sum(input1))