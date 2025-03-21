def one_and_two(seq):
    right = mul(seq)
    left = 1
    for idx, elem in enumerate(seq):
        right /= elem
        left *= elem
        if left == right:
            return idx + 1
    return -1

def mul(seq):
    result = 1
    for elem in seq:
        result *= elem
    return result 

if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        input()
        seq = list(map(int, input().split()))
        print(one_and_two(seq))
    
        