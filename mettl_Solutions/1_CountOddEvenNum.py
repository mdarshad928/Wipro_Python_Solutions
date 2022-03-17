"""Write a function to count how many out of 5 inputs are even and odd. return the count as per 6th input"""


def OddEveSum(input1: int, input2: int, input3: int, input4: int, input5: int, input6: str)->int:
    #Pastable code Starts from here
    count = 0
    totalInp = 5
    if input1%2 != 0:
        count += 1
    if input2%2 != 0:
        count += 1
    if input3%2 != 0:
        count += 1
    if input4%2 != 0:
        count += 1
    if input5%2 != 0:
        count += 1
    if input6.lower() == "odd":
        return (count)
    if input6.lower() == "even":
        return (totalInp - count) 
    #Pastable code ends here

if __name__ == "__main__":
    input1 = int(input("Enter a Number: "))
    input2 = int(input("Enter a Number: "))
    input3 = int(input("Enter a Number: "))
    input4 = int(input("Enter a Number: "))
    input5 = int(input("Enter a Number: "))
    input6 = (input("Enter Odd or Even: "))
    print(OddEveSum(input1,input2,input3, input4, input5, input6))