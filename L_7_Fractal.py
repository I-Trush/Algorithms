import graphics as gr

window = gr.GraphWin("game", 900, 900)
alpha = 0.09  # параметр уменьшающий длинну стороны квадрата


def fractal_rec(A, B, C, D, rec_deep=100):
    if rec_deep < 1:
        return  # если мы оказались ниже, значит return не случился, в итоге else можно не писать. это выход из рекурсии
    """
    gr.Line(gr.Point(*A), gr.point(*B)).draw(window)    #рисует линию из точки А в точку B и выводит ее на экран .draw(window)
    gr.Line(gr.Point(*B), gr.point(*C)).draw(window)
    gr.Line(gr.Point(*C), gr.point(*D)).draw(window)
    gr.Line(gr.Point(*D), gr.point(*A)).draw(window)    #нарисовали квадрат
    """
    for M, N in (A, B), (B, C), (C, D), (D, A):  # или ресуем циклом квадрат
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)

    A1 = (A[0] * (1 - alpha) + B[0] * alpha, A[1] * (1 - alpha) + B[1] * alpha)
    B1 = (B[0] * (1 - alpha) + C[0] * alpha, B[1] * (1 - alpha) + C[1] * alpha)
    C1 = (C[0] * (1 - alpha) + D[0] * alpha, C[1] * (1 - alpha) + D[1] * alpha)
    D1 = (D[0] * (1 - alpha) + A[0] * alpha, D[1] * (1 - alpha) + A[1] * alpha)

    fractal_rec(A1, B1, C1, D1, rec_deep - 1)


fractal_rec((100, 100), (500, 100), (500, 500), (100, 500))
