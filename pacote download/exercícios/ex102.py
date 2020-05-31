def fatorial(n, show=False):
    """
    > CALCULE O FATORIAL DE UM NUMERO
    :param n: O numero a ser calculado
    :param show: (opcional) Mostrar a conta
    :return: o valor do fatorial de um numero
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))