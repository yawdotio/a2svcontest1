def shirt_sizes(s1, s2):
    if s1 == s2:
        print("=")
    
    weights = {
        "L": 1,
        "M": 0,
        "S": -1
    }

if __name__ == "__main__":
    n = int()

    for _ in n:
        shirt1, shirt2 = input().split()
        shirt_sizes(shirt1, shirt2)