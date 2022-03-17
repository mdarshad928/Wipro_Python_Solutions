def identify_palindrome_words(input1):
  # Code Starts from here
  s = []   
  new = input1.split()
  for string in new:
    if len(string)>2:
      string = string.lower()
      reverse = ""
      i = len(string)-1
      while i>=0:
        reverse += string[i]
        i -= 1
      
      if reverse == string:
        s.append(string)
  return (len(set(s)))
  # Code ends here

if __name__ == "__main__":
  print(identify_palindrome_words("what is going to happen when Malayalam is level and peep is Tenet"))
# This will return 4