# A = [2,4,6,8,9] #4
B = [1, 2, 3, 5, 8, 9]  # 5
# D = [2,4,6,8,9,1,2,3,5,8,9]
A = list(range(10, 20)) + list(range(0, 10))

D = [4, 2, 5, 1, 3]


# print(3//2) #1


def hoart_sort(A):
    if len(A) <= 1:
        return A
    L, M, R = [], [], []
    # barier = A[len(A)//2]
    barier = A[0]
    j = k = m = 0
    for i in range(len(A)):
        if A[i] < barier:
            L.append(A[i])
        elif A[i] > barier:
            R.append(A[i])
        else:
            M.append(A[i])

    left = hoart_sort(L)
    right = hoart_sort(R)
    A = left + M + right
    return A


def hoart_sort_TF(A):
    if len(A) <= 1:
        return A
    barier = A[0]
    L, M, R = [], [], []
    for x in A:  # индексы неважны
        if x < barier:
            L.append(x)
        elif x > barier:
            R.append(x)
        else:
            M.append(x)

    left = hoart_sort(L)
    right = hoart_sort(R)
    """
    k = 0
    for x in left+M+right:
        A[k] = x
        k+=1
    """
    A = left + M + right
    return A


print(hoart_sort(A))


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
    test_sort(hoart_sort)
    #test_sort(hoart_sort_TF)


"""
