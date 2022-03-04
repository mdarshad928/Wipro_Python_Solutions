def hillWeight(input1: int, input2: int, input3: int):
    # Pastable Code Starts from here
    ans = 0
    for i in range(1, inpu1+1):
      ans = ans + input2*i
      input2 = input2 + input3
    return ans
    # Pastable Code ends here

if __name__ == "__main__":
    print(hillWeight(4,1,5))