def array_search(A: list, x: int):
    """ ищет число х в массиве А
        от 0 до N-1 индекса вклочительно
        возвращает индекс элемента х в массиве А
        или -1 если такого нет
    """
    for k in range(len(A)):
        if A[k] == x:
            return k


def invert_array(A):
    """обращение массива
    """
    B = []
    for k in range(len(A) - 1, -1, -1):
        print(k)
        print(A[k])
        B.append(A[k])
    return B


def cicle_left(A):
    """циклический сдвиг влево
    """
    x = A[0]
    for k in range(len(A) - 1):
        A[k] = A[k + 1]
    A[len(A) - 1] = x
    return A


def cicle_right(A):
    """циклический сдвиг вправо
    """
    x = A[len(A) - 1]
    for k in range(len(A) - 1, -1, -1):
        A[k] = A[k - 1]
    A[0] = x
    return A


def eratosfen(N):
    A = [True] * N
    # A[0] = A[1] = False
    for k in range(2, N):
        if A[k]:  # это и так true
            for m in range(2 * k, N, k):
                A[m] = False
    # A[0] = A[1] = False
    for k in range(N):
        print(k, "-", 'простое' if A[k] else 'составное')


if __name__ == '__main__':
    def test_array():
        A1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        m = cicle_right(A1)
        print(m)


    test_array()

    N1 = int(input())
    eratosfen(N1)
