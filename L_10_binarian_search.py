# ====0,1,2,3,4,5,6,7,8,9===============17===================27=======31=================
A = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 7, 8, 8, 8, 8, 8,
     9, 9, 9, 9, 9]
B = [5, 5, 5, 5, 6, 6, 6, 7, 7, 7]
#   [0,1,2,3,4,5,6,7,8,9,10
C = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5]
#   [0,1,2,3,4,5,6,7,8,9,10
D = [0, 1, 2, 3, 4, 5]


def left_bound(A, N, L_bound=-1, R_bound=None, lst=None):  # тонкость: если написать lst = [], то он запомнит значение lst от первого вызова ф-ии
    # lst = lst or []    #так работать не будет
    if lst == None:  # а так будет
        lst = []
    if not R_bound:
        R_bound = len(A) - 1
    print("-----------------")
    print('L_bound = ', L_bound, 'значение =', A[L_bound])
    print('R_bound = ', R_bound, 'значение =', A[R_bound])
    mid = (R_bound - L_bound) // 2 + L_bound
    print('mid = ', mid, 'A[mid] = ', A[mid])
    if A[0] == N:  # если это 1й элемент
        print("нижняя граница найдкна", L_bound)
        lst.append(L_bound)
    elif R_bound - L_bound == 1 and A[R_bound] == N:
        print("нижняя граница найдена", L_bound, A[L_bound], 'след. эл-т',
              A[L_bound + 1])  # в этой точке ответ найден, осталось его приподнять в стек
        lst.append(L_bound)
    elif A[mid] < N:
        L_bound = mid  # если мы нашли что-то меньше, то двигаемся вправо
        print('L_bound = mid ', L_bound)
        left_bound(A, N, L_bound, R_bound, lst)
    else:
        R_bound = mid
        print('R_bound = mid ', R_bound)  # если нашли что-то больше или равно, то двигаемся влево
        left_bound(A, N, L_bound, R_bound, lst)
    print(L_bound, R_bound)
    return lst[0]


"""
print("================================")        
print('A 26 <==',left_bound(A,5))
print("================================")  
print('B -1 <==',left_bound(B,5))
print("================================")  
print('C  3 <==',left_bound(C,5))
print("================================")  
print('D  4 <==',left_bound(D,5))
"""


def right_bound(A, N, L_bound=0, R_bound=None, lst1=None):
    if lst1 == None:
        lst1 = []
    if not R_bound:
        R_bound = len(A)
    mid = (R_bound - L_bound) // 2 + L_bound

    if A[len(A) - 1] == N:
        print("верхняя граница найдена", R_bound)
        lst1.append(R_bound)
    elif R_bound - L_bound == 1 and A[L_bound] == N:
        print("верхняя граница найдкна", R_bound, A[R_bound], 'пред. эл-т', A[R_bound - 1])
        lst1.append(R_bound)
    elif A[mid] > N:
        R_bound = mid  # если мы нашли что-то больше, то двигаемся влево
        right_bound(A, N, L_bound, R_bound, lst1)
    else:
        L_bound = mid
        right_bound(A, N, L_bound, R_bound, lst1)
    print(L_bound, R_bound)
    return lst1[0]


"""
print("================================") 
print('A 31 <==',right_bound(A,5))
print("================================") 
print('B 4 <==',right_bound(B,5))
print("================================") 
print('C 11 <==',right_bound(C,5))
print("================================") 
print('D 6 <==',right_bound(D,5))

"""


def binarian_search(A, N):
    L = left_bound(A, N)
    R = right_bound(A, N)
    return L, R

if __name__=='__main__':
    print("================================")
    print('A 26 31 ', binarian_search(A, 5))
    print("================================")
    print('B -1 4 ', binarian_search(B, 5))
    print("================================")
    print('C 3 11 ', binarian_search(C, 5))
    print("================================")
    print('D 4 6', binarian_search(D, 5))


# ======================================================================================

def test(A, N):
    for i in range(len(A)):
        if A[i] == N:
            print('-----')
            print('i-1 =', i - 1, '//A[i-1] =', A[i - 1])
            break


# test(A,5)


"""

def left_bound(A, N, L_bound = - 1, R_bound = None):
    if not R_bound:
        R_bound = len(A)
    mid = (R_bound - L_bound) // 2 + L_bound

    if A[0] == N:  #если это 1й элемент
        print("нижняя граница найдена", L_bound)
        return L_bound     #тогда граница = -1
    if L_bound - R_bound == 1 and A[R_bound] == N:
        print("нижняя граница найдкна", L_bound, A[L_bound], 'след. эл-т', A[L_bound+1])
        return L_bound
    if A[mid] < N:
        L_bound = mid  #если мы нашли что-то меньше, то двигаемся вправо
        left_bound(A, N, L_bound, R_bound)
    else:
        R_bound = mid
        left_bound(A, N, L_bound, R_bound)
    print(L_bound, R_bound)
    return L_bound


def left_bound(A, N, L_bound = 0, R_bound = None):

    if not R_bound:
        R_bound = len(A)-1
    print("==============")
    print('L_bound = ', L_bound, A[L_bound])
    print('R_bound = ', R_bound, A[R_bound])
    mid = (R_bound - L_bound) // 2 + L_bound
    print('mid = ', mid, 'A[mid] = ', A[mid])
    if A[L_bound] == N:  #если это 1й элемент
        print("нижняя граница найдкна", L_bound)
        return L_bound     #тогда граница = -1
    elif R_bound - L_bound == 1 and A[R_bound] == N:
        print("нижняя граница найдкна", L_bound, A[L_bound], 'след. эл-т', A[L_bound+1])
        return L_bound
    elif A[mid] < N:
        L_bound = mid  #если мы нашли что-то меньше, то двигаемся вправо
        print('L_bound = mid ' ,L_bound)
        left_bound(A, N, L_bound, R_bound)
    else:
        R_bound = mid
        print('R_bound = mid ' ,R_bound)  #если нашли что-то больше или равно, то двигаемся влево
        left_bound(A, N, L_bound, R_bound)
    print(L_bound, R_bound)
    return L_bound


def left_bound(A, N, L_bound = 0, R_bound = None):
    if not R_bound:
        R_bound = len(A)
    print("==============")
    print('L_bound = ', L_bound)
    print('R_bound = ', R_bound)
    mid = (R_bound - L_bound) // 2 + L_bound
    #print('mid = ', mid, 'A[mid] = ', A[mid])
    if A[L_bound] == N:  #если это 1й элемент
        print("нижняя граница найдкна", L_bound)
        return L_bound     #тогда граница = -1
    if L_bound == R_bound - 1:
        print("нижняя граница найдкна", L_bound, A[L_bound], 'след. эл-т', A[L_bound+1])
        return L_bound
    if A[mid] < N:
        L_bound = mid  #если мы нашли что-то меньше, то двигаемся вправо
        print('L_bound = mid ' ,L_bound)
        #left_bound(A,N,L_bound)
        left_bound(A, N, L_bound, R_bound)
    else:
        R_bound = mid
        print('R_bound = mid ' ,R_bound)  #если нашли что-то больше или равно, то двигаемся влево
        left_bound(A, N, L_bound, R_bound)


def right_bound(A, N, L_bound = 0, R_bound = None):
    if not R_bound:
        R_bound = len(A)-1
    mid = (R_bound - L_bound) // 2 + L_bound
    if A[R_bound] == N: 
        print("верхняя граница найдена", R_bound +1)
        return R_bound +1     #это последний эл-т
    if L_bound + 1 == R_bound:
        print("верхняя граница найдкна", R_bound, A[R_bound], 'пред. эл-т', A[R_bound-1])
        return R_bound
    if A[mid] > N:
        R_bound = mid  #если мы нашли что-то больше, то двигаемся влево
        right_bound(A, N, L_bound, R_bound)
    else:
        L_bound = mid
        right_bound(A, N, L_bound, R_bound)
    return R_bound

def binarian_search(A,N):
    L = left_bound(A,N)
    R = right_bound(A,N)
    return L,R


print('A 19 24 ', binarian_search(A,5))
print('B -1 4 ', binarian_search(B,5))
print('D 3 11 ', binarian_search(D,5))
print('E 4 6',  binarian_search(E,5))


print(right_bound(A,5))
print(right_bound(B,5))
print(right_bound(D,5))
print(right_bound(E,5))


left_bound(A,5)
left_bound(B,5)
left_bound(D,5)
left_bound(E,5)
"""
