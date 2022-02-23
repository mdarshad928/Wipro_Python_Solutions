n = int(input("Enter the number of lines you want to read: "))
f1 = open('file.txt', 'r')
for i in range(n):
  print(f1.readline(), end="")
print()
f1.close()