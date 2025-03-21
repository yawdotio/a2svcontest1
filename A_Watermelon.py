import math 

def watermelon(size):
    for i in range (2, size, 2):
        if (size % i) % 2 == 0:
            print("YES")
            return 
    print("NO")
    return 

if __name__ == "__main__":
    watermelon(int(input()))