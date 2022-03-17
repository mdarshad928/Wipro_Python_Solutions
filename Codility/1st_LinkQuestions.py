# Question 1
def solution(N):
    # write your code in Python 3.6
    for i in range(N-1):
        print("L")
    for i in range(N):
        print("L", end="")

# Question 2
def solution(A):
    # write your code in Python 3.6
    minimum = 11000
    for i in A:
        if i<minimum and i%11 == 0:
            minimum = i
    return minimum