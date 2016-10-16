def fib(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib(i-2)+fib(i-1)

if __name__ == "__main__":
    N = int(input().strip())
    pow3 = lambda X: X*X*X
    print(list(map(pow3, [fib(i) for i in range(N)])))