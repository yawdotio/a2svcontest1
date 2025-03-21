def wrongaddition(num1, num2):
    length1 = len(num1)

    position2 = -1
    end2 = - 2

    result = ""

    for position in range(length1 - 1 , 0, -1):
        while num1[position] < num2[position2:end2:-1]:
            print(num2[position2:end2:-1])
            print(num1[position])
        result += str(int(num2[position2: end2:-1]) - int(num1[position]))
        position2 = end2 -1
        end2 = position2 -1
    print(result)

if __name__ == "__main__":
    n = int(input())
    
    for _ in range(n):
        num1, num2 = input().split()
        wrongaddition(num1, num2)