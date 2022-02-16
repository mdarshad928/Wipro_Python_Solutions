string = input("Enter a string: ")
reverse = ""
i = len(string)-1
while i>=0:
  reverse += string[i]
  i -= 1

if reverse == string:
  print("It's a palindrome")
else:
  print("It's not a palindrome")