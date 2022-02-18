def evenPrint(alist):
  evenList = []
  for i in alist:
    if i%2 == 0:
      evenList.append(i)
  return evenList


if __name__ == "__main__":
  sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  print("Sample List: ", sample_list)
  print("List of even numbers: ", evenPrint(sample_list))