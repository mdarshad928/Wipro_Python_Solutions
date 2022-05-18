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



###### JAVA SOLUTION #####
# public class Main
# {
# 	public static int solution(int N){
# 	    String str = Integer.toString(N);
# 	    int count = str.length() - str.replace("5","").length();
# 	    int index = -1;
# 	    int max = Integer.MIN_VALUE;
# 	    for (int i = 0; i<count; i++){
# 	        index = str.indexOf("5", index+1);
# 	        String s = str.substring(0,index)+str.substring(index+1, str.length());
# 	        if (Integer.parseInt(s)>max){
# 	            max = Integer.parseInt(s);
# 	        }
# 	    }
# 	    return max;
# 	}
	
# 	public static void main(String[] args) {
# 		System.out.println(solution(5000));
# 	}
# }