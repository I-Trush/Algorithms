# A = [2,4,6,8,9] #4
B = [1, 2, 2, 3, 5, 8, 9]  # 5
# D = [2,4,6,8,9,1,2,3,5,8,9]
A = list(range(10, 20)) + list(range(0, 10))

D = [9, 8, 7, 6, 5, 4, 2, 1]


# print(3//2) #1


def verification_sort(A, ascending=True):
    """ проверка отсортированности массива за О(N)"""

    def ascending_f(x0, x1, ascending):
        if ascending:
            return x0 > x1  # по возрастанию
        else:
            return x0 < x1  # по убыванию

    if len(A) <= 1:
        print('array is sorted')

    flag = True
    for i in range(len(A) - 1):
        if ascending_f(A[i], A[i + 1], ascending):
            flag = False
            break
    print('array is sorted' if flag else 'not sorted')


print('B', B)
verification_sort(B)

print('D', D)
verification_sort(D, False)

print('D', A)
verification_sort(A)

print('D', A)
verification_sort(A, False)


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
