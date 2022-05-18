def insertionSort(arr):
  for i in range(1, len(arr)):
    value = arr[i]
    hole = i
    while hole>0 and arr[hole-1]>value:
      arr[hole] = arr[hole-1]
      hole -= 1
    arr[hole] = value
  return arr

if __name__ == '__main__':
  print(insertionSort([6, 3, 7, 5, 8, 8, 9, 3]))