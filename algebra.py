def diviseurs(n):
    return [i for i in range(1, n + 1) if n % i == 0]


def est_premier(n):
    return len(diviseurs(n)) == 2
