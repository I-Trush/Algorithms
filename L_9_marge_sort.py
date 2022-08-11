# A = [2,4,6,8,9] #4
B = [1, 2, 3, 5, 8, 9]  # 5
# D = [2,4,6,8,9,1,2,3,5,8,9]
A = list(range(10, 20)) + list(range(0, 10))

D = [4, 2, 5, 1, 3]


# print(3//2) #1

def merge(A: list, B: list):
    C = [0] * (len(A) + len(B))  # подготовили массив С нужной длины (зарезервировали нужное кол-во памяти)
    i, k = 0, 0
    for j in range(len(C)):
        # print(i,k)
        if i == len(A):
            C[j] = B[k]
        elif A[i] <= B[k]:
            C[j] = A[i]
            i += 1
        else:
            C[j] = B[k]
            k += 1
    return C


# print(merge(A,B))


def merge_sort(D):
    # sep = len(D)//2

    if len(D) <= 1:
        return D
    sep = len(D) // 2
    L = merge_sort(D[:sep])
    R = merge_sort(D[sep:])

    X = merge_prepod(L, R)
    D = X[:]
    return D


"""
def merge_sort(A):
    if len(A) == 1 or len(A) == 0:
        return A
    L = merge_sort(A[:len(A) // 2])
    R = merge_sort(A[len(A) // 2:])

    n = m = k = 0
    C = [0] * (len(L) + len(R))
    while n < len(L) and m < len(R):
        if L[n] <= R[m]:
            C[k] = L[n]
            n += 1
        else:
            C[k] = R[m]
            m += 1
        k += 1
    while n < len(L):
        C[k] = L[n]
        n += 1
        k += 1
    while m < len(R):
        C[k] = R[m]
        m += 1
        k += 1
    #for i in range(len(A)):
     #   A[i] = C[i]
    A=C[:]
    return A
"""


# ==========================================================================================================
def merge_prepod(L: list, R: list):
    n = m = k = 0
    C = [0] * (len(L) + len(R))
    while n < len(L) and m < len(R):
        if L[n] <= R[m]:
            C[k] = L[n]
            n += 1
        else:
            C[k] = R[m]
            m += 1
        k += 1
    while n < len(L):
        C[k] = L[n]
        n += 1
        k += 1
    while m < len(R):
        C[k] = R[m]
        m += 1
        k += 1
    return C


print(merge_sort(A))
print(merge_sort(B))
print(merge_sort(D))


# print(merge_prepod(A,B))
# ===============================================================================================================
def test_sort(sort_algorithm):
    print("тестируем: ", sort_algorithm.__doc__)  # так выглядит доступ к документ-строке тестовой ф-иии
    print("test 1:", end="")
    D = [4, 2, 5, 1, 3]
    D_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(D)
    print("ok" if D == D_sorted else 'fail')

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


"""
if __name__=='__main__':
    test_sort(merge_sort)
    #test_sort(insert_sort_prepod)


"""
