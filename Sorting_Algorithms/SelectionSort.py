def SelectionSortW(arr):   # [4 5 2 7 4 8 1] Using while loop
  length = len(arr)
  i = 0
  while i < length-1:
    min = i
    j = i+1
    while j<length:
      if arr[j] < arr[min]:
        min = j
      j += 1
    arr[i], arr[min] = arr[min], arr[i]
    i += 1
  return arr



def SelectionSortF(arr):   # [4 5 2 7 4 8 1] Using for loop
  length = len(arr)
  i = 0
  for i in range(length-1):
    min = i
    j = i+1
    for j in range(i,length):
      if arr[j] < arr[min]:
        min = j
    arr[i], arr[min] = arr[min], arr[i]
  return arr

if __name__ == '__main__':
  print(SelectionSortF([6, 3, 7, 5, 8, 8, 9, 3]))