N = int(input())



def fivemultiple(num):
    string_num = str(num)
    int_num = int(string_num[0]) + int(string_num[1])
    if int_num % 5 == 0:
        return True
    else:
        return False 

if N % 2 == 0 and fivemultiple(N):
    print("Yes")
else:
    print("No")