longest = ""
f1 = open('file.txt')
x = f1.readlines()
t = []
for i in x:
  t += i.split()
  for j in t:
    if len(j.rstrip('.'))>len(longest):
      longest = j
f1.close()
print("The Longest word is: ",longest)