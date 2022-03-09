# x = 'wipro'
# y = 12                            # Variable naming         
# # b = False
# # f = 12.5
# # l = []
# # s = set()
# # d = dict()
# # t = tuple()

# # print(type(x))
# # print(type(y))
# # print(type(b))
# # print(type(f))
# # print(type(l))
# # print(type(s))
# # print(type(d))
# # print(type(t))

# # arithmatic operator
# # addition(+)  subtraction(-) multiplication(*) division(/) (//) modulo(%)

# x = 5  #concatenation      
# y = 3              # = assignment operator                                        
# # z = x%y        # remainder 
# # print(z)
# # print(type(z))
# '''wipro is a MNC company

# its headquarted in bangalore.'''

# # Relation operator

# if x is y:             # == checks for equality          Relational operator output-->>  True/False 
#   print("yes they are equal")               
# # elif x<y:                            #<=, >=
# #   print("x is less than y")
# # elif x>y:              # >
# #   print("x is greater than y")
# elif x is not y:                        # is not   !=
#   print("x and y is not equal")

# t = [1, 2, 3]
# u = [1, 2, 3]

# if t == u:             # == checks for content
#   print(1)
# if t is u:              # is doesn't check content wise.
#   print(2)

# #Logical Operator

# #&&(and) ||(or) !(not)  

# q = 7
# w = 5
# r = 5

# if (r == w) or (w>q):   # and or not is always used between bools.   True and True = True
#   print("conditon satisfied")                                        # True and False = False
                                                                    # False and True = False

# Bitwise Operator     a = "A"  b = "B"  65 00111000 66 00111001                 00110000 

# Shift Operator     Operator Precedence


# x = (input("Enter a name. "))
# t = 3.2                 # Variable == literal
# i = int(t)
# y = 12                      # str()  float() int()   bool()
# print(i, type(i), type(y))    # Implicit = Jo dikhta nahi hai.   Explicit = jo dikhta hai.


# for i in range(1,11,1): 
#   print(i, sep = "@", end = "\t")       # \n new line character string
                                                  # \t
# print("******************")
# print("\t arshad")                                      # \ escape character
# print("******************")

# i = 1
# while i<11:                            # 1<11
#       print(i)
#       i += 1                 # i = i + 1
# print(i)

# ******************************* List ****************************
# x = [1, 4, 5, 6, 6]      # Mutable, Ordered, Indexed, Duplicate       "Difference b/w Array and List"
# print(dir(x))
# x.append([1, 2, 4])
# x.clear()
# y = x.copy()

# print(x.count(6))
# x.extend([1,3,4,7])
# print(x)
# print(x.index(1,4))
# x.insert(2, "aman")
# print(x)
# x.pop(1)
# x.remove("wipro")
# print(x)
# x.reverse()
# print(x)
# x.sort(reverse = True)
# print(x)

# ******************* TUPLE **************************
# x = (12, 34, 11, 19, 12)                              #Immutable, Indexed, Ordered, Duplicate
# print(dir(x))

# # Swap the variable

# t = 12
# u = 35
# print(t, u)

# u, t = t, u
# print(t, u)
# x = range(1)
# print(dir(x))
# for i in "wipro":
#   print(dir(i))


# ******************** Dictionary(HashMap) *********************

# Key:Value                            # Mutable, UnIndexed, Unordered, Duplicate Key is not allowed
# d = { 2:5, 0:"aman", "arshad":"wipro"}
# print(dir(d))
# for key in d:
#   print(key)
# print(d.clear())
# print(d)
# nd = d.copy()
# print(d, nd)
# print(d.fromkeys("aman", 3))
# print(d)
# print(d.get(2))
# print(d[2])
# t = (d.items())
# for i in d.keys():
#   print(i)
# p = d.pop(0)
# print(p, d)
# print(d)
# print(d.popitem())
# (d.setdefault(2))
# print(d)
# new = {"first": "smart", "second":"clever"}
# d.update(new)
# print(d)
# print(d+new)

# in keyword

# if 0 in d:
#   print("yes")
# ********************** Set **********************

# s = {1, 2, 3, 4, 4}                       # Immutable, Unindexed, Unordered, Duplicate not allowed
# # print(type(s))
# print(dir(s))
# s[0] = 5
# print(s)

# ********************** String ****************************

# s = 'mdArshad928@gmail.com'
# print(dir(s))
# print(s.capitalize())                                    # calling the method
# print(s.casefold())
# print(s.count("u"))                                        # b'Suraj'
# t = s.encode()
# print(type(t))
# print(s.endswith("j"))
# print(s.find("x"))
# print(s.index("a", 3))
# print(s.isdecimal())
# print(s.isalpha())
# print(s.islower())
# print(s.isupper())
# print(s.lower())
# print(s.upper())
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())
# print(s.split("@"))

# print(s[12:23])                 # string slicing

# ***************** Functions ***********************
# x = 2
# def Myprint(*args):     # Signature of Function   
#   print(args)
#   print((args[0]))
#   return


# x = Myprint("aman", "suraj")                    # None (Null)
# print(x)


# Given a number, Check whether it is a palindrome or not using while loop

# num = int(input("Enter a number: "))        # 123456    , 1234, 123, 12, 1, 0

# l = len(str(num))-1
# numcopy = num                                  
# new = 0
# while numcopy>0:                                            # 6*100000 + 5*10000 + 4*1000 + 3*100 + 2*10 + 1
#     new = new + (numcopy%10)*(10**l)
#     l -= 1
#     numcopy = numcopy//10

# if new == num:
#     print("Yes")
# else:
#     print("No")



# *************** Module & Package **********************
  # Function, Class
def createPassword(input1: str, input2: str):
  # Pastable Code starts from here
  password = ""
  part1, part2, part3 = makeParts(input1)
  password += part2
  part1, part2, part3 = makeParts(input2)
  password += part2 + part1
  return password

def makeParts(inp: str):
  check = len(inp)%3

  if check == 0:
      part1 = inp[0:len(inp)//3]
      part2 = inp[len(inp)//3:-len(inp)//3]
      part3 = inp[-len(inp)//3:len(inp)]
  elif check == 1:
      part1 = inp[0:len(inp)//3]
      part2 = inp[len(inp)//3:-len(inp)//3+1]
      part3 = inp[-len(inp)-1//3:len(inp)]
  else:
      part1 = inp[0:len(inp)//3+1]
      part2 = inp[len(inp)//3+1:-len(inp)//3]
      part3 = inp[-len(inp)//3:len(inp)]
  return part1, part2, part3

if __name__ == "__main__":
  print(createPassword("WIPRO", "TECHNOLOGIES"))