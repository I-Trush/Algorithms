def fib(n):
    A = []
    A.append(0)
    A.append(1)
    for i in range(2, n + 1):
        A.append(A[i - 1] + A[i - 2])
        print(A)
        print(i)
    return A[n]


# print(fib(int(input())))
