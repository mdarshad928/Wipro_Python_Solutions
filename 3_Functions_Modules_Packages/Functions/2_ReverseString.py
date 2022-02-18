def RevStr(string):
  reverse = ""
  i = len(string)-1
  while i>=0:
    reverse += string[i]
    i -= 1
  return reverse

if __name__ == "__main__":
  string = input("Enter a string: ")
  print(RevStr(string))