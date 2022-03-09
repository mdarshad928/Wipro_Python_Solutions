def secondWordUpperCase(input1: str):
  # Pastable Code Starts from here
  wordList = input1.split()
  if len(wordList)<2:
    return "LESS"
  else:
    return wordList[1].upper()
  # Pastable Code ends here.

if __name__ == "__main__":
  print(secondWordUpperCase(input("Enter a sentence: ")))