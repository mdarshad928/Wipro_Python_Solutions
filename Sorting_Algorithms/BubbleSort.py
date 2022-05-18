def bubbleSort(arr):
  for i in range(len(arr)):
    flag = 0
    for i in range(len(arr)-i-1):
      if arr[i+1] < arr[i]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        flag == 1
    if flag == 1:
      break
  return arr
if __name__ == '__main__':
  print(bubbleSort([6, 3, 7, 5, 8, 8, 9, 3]))