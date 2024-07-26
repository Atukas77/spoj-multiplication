def mult(a, b):
    return a*b

def main():
    n = int(input())
    values = []
    for i in range(n):
        a, b = map(int, input().split())
        values.append((a, b))
    for i in values:
        print(mult(i[0], i[1]))

main()