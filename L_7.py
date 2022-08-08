def fact(n: int):
    if n <= 1:
        return 1

    return fact(n - 1) * n


# print(fact(int(input())))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


a = 2
n = 4
# print(gcd(a,b))


def degree(a, n):
    if n <= 0:
        return 1
    return degree(a, n - 1) * a


print(degree(a, n))
