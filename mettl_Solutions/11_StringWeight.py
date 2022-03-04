def stringWeight(input1: str, input2: int):
  # Pastable Code starts from here
    vowel = []
    const = []
    for i in input1.upper():
        asc = ord(i)
        if asc in [65, 69, 71, 82, 85]:
            vowel.append(asc - 64)
        elif asc>64 and asc<97:
            const.append(asc-64)
    
    if input2 == 0:
        return (sum(const))
    elif input2 == 1:
        return (sum(vowel + const))

  # Pastable Code ends here

if __name__ == "__main__":
    print(stringWeight(input(), int(input())))