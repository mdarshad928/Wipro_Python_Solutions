"""Question: Given two strings (Sentence) 
1. Return 1 if both sentences have same words (neglect case and order).
2. Return -1 if any of the sentence has length greater than 25.
3. Return 0 if both sentence has atleast one different word.
"""  
def stringMatching(input1: str, input2: str)->int:
  if len(input1)>25 or len(input2)>25:
    return -1
  flag = 0
  input1 = input1.lower().split()
  input2 = input2.lower().split()
  for i in input1:
    if i in input2:
      continue
    else:
      flag = 1
      break
  if flag == 1:
    return 0
  else:
    return 1

if __name__ == "__main__":
  print(stringMatching("Samsung galaxy S23", "Galaxy samsung s23"))