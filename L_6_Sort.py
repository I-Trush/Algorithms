def insert_sort(A):
    """сортировка вставками"""
    for top in range(1, len(A)):
        for k in range(len(A[0:top]), -1, -1):
            if k > 0 and A[k] < A[k - 1]:
                A[k], A[k - 1] = A[k - 1], A[k]
                # print(A)


def insert_sort_TF(A):
    """сортировка вставками препод"""
    for top in range(1, len(A)):
        k = top
        while k > 0 and A[k] < A[k - 1]:  # проход вниз по элементам массива осущ. за счет понижения k
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1
            # print(A)


# ====================================================================================================
def mymin(A):
    """ доп ф-ия для поиска минимума"""
    x = 0
    res = A[x]
    for i in range(1, len(A)):
        if res > A[i]:  # если вдруг наш элемент больше, чем i-й, то записать i-й элемент
            res = A[i]
            x = i
    return x


def choise_sort(A):
    """ сортировка выбором, сперви ищит самого маленького mymin(A) и отправляет его в начало
        после чего первый элемент уже не трогает
        сортирует оставшуюся часть
        и так по циклу до конца
    """
    for m in range(len(A)):
        # print(m)
        # print(A[m:])
        x = mymin(A[m:])
        A[m], A[x + m] = A[x + m], A[m]  # x+m нужно, чтобы при уменьшеном массиве запомнить позицию в большом массиве
        # print(A)


def choise_sort_TF(A):
    """
        препод читер
    """
    N = len(A)
    for pos in range(0, N - 1):
        for k in range(pos + 1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]
                # print(A)


# ====================================================================================================
def bubble_sort(A):
    """ пузырьковая сортировка"""
    N = len(A)
    m = 1
    while m < N:  # N-1 проход, поэтому строгое неравенсто
        for k in range(N - m):
            if A[k] > A[k + 1]:
                A[k], A[k + 1] = A[k + 1], A[k]
        m += 1
        # print(A)


def bubble_sort_TF(A):
    """ пузырьковая сортировка от препода"""
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N - bypass):
            if A[k] > A[k + 1]:
                A[k], A[k + 1] = A[k + 1], A[k]


# ====================================================================================================
A = [3, 4, 5, 6, 7, 8, 3, 4, 5, 6, 1, 2, 3, 4, 9, 7, 5, 4]
C = {1: 1, 2: 2}
print(C.get(4))


def count_sort(A):
    """ сортировка подсчётом
        странно, почему-то в python 2.10 ключи словаря в виде цифр оказываются в том порядке, в котором их туда вносили
        хотя в python 3.7 они были упорядоченны по возрастанию (что логичнее для быстрого поиска)
    """
    B = {}
    for k in range(len(A)):
        if B.get(A[k]) == None:
            B[A[k]] = 1
        else:
            B[A[k]] += 1
        print(B)


count_sort(A)


def test_sort(sort_algorithm):
    print("тестируем: ", sort_algorithm.__doc__)  # так выглядит доступ к документ-строке тестовой ф-иии
    print("test 1:", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("ok" if A == A_sorted else 'fail')

    print("test 2:",
          end="")  # такое окончание строки end="" приведет к тому, что следующий оператор принт окажется в этой строке
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(0, 10)) + list(range(10, 20))
    sort_algorithm(A)
    print("ok" if A == A_sorted else 'fail')

    print("test 3:", end="")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print("ok" if A == A_sorted else 'fail')



if __name__=='__main__':
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(bubble_sort)
    test_sort(insert_sort_TF)
    test_sort(choise_sort_TF)
    test_sort(bubble_sort_TF)


