def createPassword(input1: str, input2: str):
  # Pastable Code starts from here
  password = ""
  check = len(input1)%3

  if check == 0:
      part1 = input1[0:len(input1)//3]
      part2 = input1[len(input1)//3:-len(input1)//3]
      # part3 = input1[-len(input1)//3:len(input1)]
  elif check == 1:
      part1 = input1[0:len(input1)//3]
      part2 = input1[len(input1)//3:-len(input1)//3+1]
      # part3 = input1[-len(input1)-1//3:len(input1)]
  else:
      part1 = input1[0:len(input1)//3+1]
      part2 = input1[len(input1)//3+1:-len(input1)//3]
      # part3 = input1[-len(input1)//3:len(input1)]
  password += part2
  
  check = len(input2)%3

  if check == 0:
      part1 = input2[0:len(input2)//3]
      part2 = input2[len(input2)//3:-len(input2)//3]
      # part3 = input2[-len(input2)//3:len(input2)]
  elif check == 1:
      part1 = input2[0:len(input2)//3]
      part2 = input2[len(input2)//3:-len(input2)//3+1]
      # part3 = input2[-len(input2)-1//3:len(input2)]
  else:
      part1 = input2[0:len(input2)//3+1]
      part2 = input2[len(input2)//3+1:-len(input2)//3]
      # part3 = input2[-len(input2)//3:len(input2)]
  password += part2 + part1
  return password
  # Pastable Code ends here


if __name__ == "__main__":
  print(createPassword("WIPRO", "TECHNOLOGIES"))



######################## Short Version(not for mettl) ############################


# def createPassword(input1: str, input2: str):
#   password = ""
#   part1, part2, part3 = makeParts(input1)
#   password += part2
#   part1, part2, part3 = makeParts(input2)
#   password += part2 + part1
#   return password

# def makeParts(inp: str):
#   check = len(inp)%3

#   if check == 0:
#       part1 = inp[0:len(inp)//3]
#       part2 = inp[len(inp)//3:-len(inp)//3]
#       part3 = inp[-len(inp)//3:len(inp)]
#   elif check == 1:
#       part1 = inp[0:len(inp)//3]
#       part2 = inp[len(inp)//3:-len(inp)//3+1]
#       part3 = inp[-len(inp)-1//3:len(inp)]
#   else:
#       part1 = inp[0:len(inp)//3+1]
#       part2 = inp[len(inp)//3+1:-len(inp)//3]
#       part3 = inp[-len(inp)//3:len(inp)]
#   return part1, part2, part3
  

# if __name__ == "__main__":
#   print(createPassword("WIPRO", "TECHNOLOGIES"))
  