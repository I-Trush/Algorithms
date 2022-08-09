def gen_num(N: int, M: int, prefix=None):
    prefix = prefix or []  # если prefix =None то будет пустой список
    if M == 0:
        print(prefix)
        return

    for digit in range(N):
        prefix.append(digit)
        gen_num(N, M - 1, prefix)  # рекурентный вызов происходит в цикле
        prefix.pop()  # удалили последнюю цифру, при этом та цифра, что сдвинулась в глубь списка остается


"""
x=int(input())
y=int(input())
gen_num(x,y)

"""


def gen_permutations(N: int, M: int = -1, prefix=None):
    """ генерация всех перестановок N чисел в M позициях
    """
    prefix = prefix or []
    if M == -1:  # типа это такой ключ был, поскольку в вызове ф-ии нельзя писать M=N
        M = N  # по умолчанию N чисел в N позициях
    if M == 0:
        print(prefix)
        return
    for number in range(1, N + 1):
        if number in prefix:
            continue
        prefix.append(number)
        gen_permutations(N, M - 1, prefix)
        prefix.pop()


"""
x=int(input())
y=int(input())
gen_permutations(x,y)
"""
