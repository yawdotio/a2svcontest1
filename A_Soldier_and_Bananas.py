def soldiers_and_bananas(k,n,w):
    borrow = 0
    count = 2
    cost = k
    while w > 0:
        n -= cost
        if n < 0:
            borrow -= n 
            n = 0
        cost = count * k
        w -= 1
        count += 1
    return borrow


if __name__ == "__main__":
    k,n,w = map(int, input().split())
    print(soldiers_and_bananas(k,n,w))