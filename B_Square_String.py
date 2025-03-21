def square(s):
    mid = len(s)//2
    if s[:mid] == s[mid:]:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        s = input()
        square(s)
