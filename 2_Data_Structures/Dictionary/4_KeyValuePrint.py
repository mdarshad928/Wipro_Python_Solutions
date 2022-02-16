dict1 = {1: 10, 2: 20, 3: 30, "org": "wipro"}

print("*********************************")
print("print keys")
for key in dict1:
  print(key)
print("*********************************")
print("print values")
for key in dict1:
  print(dict1[key])
print("*********************************")
print("print keys with value")
for key in dict1:
  print(key, " : ", dict1[key])
print("*********************************")