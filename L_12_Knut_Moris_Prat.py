# S = 'abacabadabacabafabacabadabacabadabacabafaba'
# sub = 'dabac'

def simple_search(S, sub):
    sub_len = len(sub)
    S_len = len(S)
    n = 0
    for i in range(S_len - sub_len):
        k = i + sub_len
        if S[i:k] == sub:
            n += 1
            print(i, n)
    return n


def scan(A):
    P = [0] * len(A)
    i = 1
    j = 0

    for k in range(len(A)):
        if A[i] == A[j]:
            P[i] = j + 1
            j += 1
            i += 1
        else:
            if j == 0:
                P[i] = 0
                i += 1
            else:
                j = P[j - 1]
    print(P)


# scan(A)
# print(len(A))
# ===========================================================================
# simple_search(S,sub)
# ====123456789||||||===========21
S = 'abcabeabcabcabdabcbac'
A = 'abcabd'
# ====123456
tmp = A + '#' + S
print(len(tmp))


def scan_KMP(S, A):  # при этом второе вхождение не ловится
    P = [0] * (len(A) + 1) + [0] * len(S)
    i = 1
    j = 0
    tmp = A + '#' + S
    for k in range(len(tmp)):

        if tmp[i] == tmp[j]:
            P[i] = j + 1
            j += 1
            i += 1
        else:
            if j == 0:
                P[i] = 0
                i += 1
            else:
                print('j=', j, 'P[j-1]=', P[j - 1], 'P[j]=', P[j], tmp[j], 'i=', i, tmp[i])
                j = P[j - 1]
                print('j=', j, 'P[j-1]=', P[j - 1], tmp[j], 'i=', i, tmp[i])

        print('j=', j, tmp[j], '||', 'i=', i, tmp[i], '|| P[i-1]=', P[i - 1])
    # print(P, len(P))
    for n in range(len(P)):
        print(n, tmp[n], P[n])  # в тот момент, когда P-функция возвращает 6 (эл-т = длинне искомой строки len(А)) - вхождение найдено


scan_KMP(S, A)

"""
def scan_KMP(S,A):
    P = [0]*len(S)
    i = 0
    j = 0

    for k in range(len(S)):
        if A[i] == S[j]:
            P[i] = j + 1
            j+=1
            i+=1
            print('A[i] == S[j]: =============')
            print(P)
        else:
            print('не равны ------------------')
            print(P)
            j = 0
    print(P)
"""
