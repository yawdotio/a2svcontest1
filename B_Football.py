import math 

def football(s):
    count = 1
    current = s[1]
    for i in s:
        if i == current:
            count +=1
            if count > 6:
                print("YES")
                return
        else:
            current = i
            count = 1
    print("NO")
    return 

if __name__ == "__main__":
    football(input())