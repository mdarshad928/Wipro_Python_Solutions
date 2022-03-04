def isPalindrome(input1: str):
    # Pastable Code Starts from here
    new_str = ""
    for i in range(len(input1)-1, -1, -1):
      new_str += input1[i].lower()
    if new_str == input1.lower():
      return 2
    else:
      return 1
    # Pastable Code ends here

if __name__ == "__main__":
    print(isPalindrome(input("Enter the String: ")))

