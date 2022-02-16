# 8. Write a program to remove the first occurence of a specified element from the list


list1 = [28, 100, 63, 93, 59, 100]

print("List = ", list1)

list1.remove(100) # unlike pop, when we remove method on list we provide element not the index of element
print("List after removing first occurence of 100 = ", list1)