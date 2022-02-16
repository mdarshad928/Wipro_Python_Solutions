dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

print("Sample Dictionary = ", dict1)
sum = 0
for key in dict1:
  sum = sum + dict1[key]

print("total sum of dictionary values = ", sum)