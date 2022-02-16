string = input("Enter a string: ")
length = len(string)
repeater = string[-3:length]
newStr = repeater*length
print(newStr)