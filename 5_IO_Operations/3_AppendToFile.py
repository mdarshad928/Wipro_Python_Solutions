x = input("Enter what you want to append: ")

f1 = open('file.txt','a')
f1.write("\n"+x)
f1.close()