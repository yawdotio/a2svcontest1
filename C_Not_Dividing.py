def notdividing(arr):
    arr = arr[::-1]
    result = ""

    prev = arr[0]
    result += str(prev)

    for ch in arr[1:]:
        while prev % ch == 0:
            ch += 1
        prev = ch
        result += " " + str(ch)
    print(result[::-1])
    return 


if __name__ == "__main__":
    n = int(input())
    
    for _ in range(n):
        lenght = input()
        arr = list(map(int, input().split()))
        notdividing(arr)