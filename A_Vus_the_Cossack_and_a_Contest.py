def main(n,m,k):
    if m >= n and k >= n:
        print("Yes")
    else:
      print("No")

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    main(n,m,k)