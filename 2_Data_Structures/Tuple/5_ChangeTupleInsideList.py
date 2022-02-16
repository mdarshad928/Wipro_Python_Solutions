list_of_tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

print("Sample list of tuples = ", list_of_tuples)
index = 0
for i in list_of_tuples:
  x = list(i)
  x[2] = 100
  list_of_tuples[index] = tuple(x)
  index += 1

print("Output = ", list_of_tuples)