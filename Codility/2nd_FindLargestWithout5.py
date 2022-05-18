def solution(N):
    string = str(N)
    five_count = string.count("5")
    solution_choice_list = []
    index = -1
    for i in range(five_count):
        index = string.index("5", index+1)
        solution_choice_list.append(int(string[0:index]+string[index+1:]))
    mx = max(solution_choice_list)
    if max(solution_choice_list)!=0:
        return mx 
    else:
        return 0
            


if __name__ == "__main__":
    print(solution(555555))