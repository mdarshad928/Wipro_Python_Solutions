def socksPairCount(input1: int, input2: list)->str:
  # input1 ----> int type: indicates len of list
  # input2 ----> list type: color number of sock
  hdict = {}
  pairs = 0
  for i in input2:
    if i in hdict:
      hdict[i] += 1
    else:
      hdict[i] = 1
  for key in hdict:
    pairs += hdict[key]//2
  return pairs


if __name__ == "__main__":
  print(socksPairCount(8, [10, 20, 10, 50, 20, 10, 90, 10]))