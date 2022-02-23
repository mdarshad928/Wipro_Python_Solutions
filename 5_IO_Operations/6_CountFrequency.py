#Incomplete
inp = input("Enter the word: ")
count = 0
f1 = open('file.txt')
x = f1.readlines()
t = []
for i in x:
  t = i.split()
  print("********************")
  for j in t:
    print(j)
    print(f'j is {j}, input is {inp}')
    if j == x:
      count+=1
f1.close()
print("Total Count is: ", count)