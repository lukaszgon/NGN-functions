def e_tocz_j(A_j, K, u_j):
    return (A_j / u_j * (1 + A_j**K* (K * A_j - (K+1))) / (1 - A_j) / (1 - A_j**(K+2)))


def u_j(e_tnad_j):
    return e_tnad_j**-1


def b_i(A, K):
    return ((1-A)*A**(K+1)/(1-A**(K+2)))


def e_tnad(b_cal, C):
    return b_cal/C


def ipdv_max(ipdt_max, ipdt_min):
    return ipdt_max-ipdt_min


def a_rt(c_rt, c):
    return c_rt/c


def a_nrt(c_nrt, c_rt, c):
    return c_nrt/(c-c_rt)


def lossprob(a, k):
    return (1 - a) * a ** (k + 1) / (1 - a ** (k + 2))


def erlFun(A):
    E = 1
    N = 0
    while((A * E / (N + A * E) > 0.0017)):
        N += 1
        E = A * E / (N + A * E)
        print('N = ', N, ' E = ', E)


def ipdt_max_rt(k1, e_tnad_rt, e_tnad_nrt):
    return sum([k1 * x for x in e_tnad_rt]) + sum(e_tnad_nrt)


def ipdt_max_nrt(k2, e_tnad_nrt, a1):
    return sum([(k2 + 1) * x / (1 - a1) for x in e_tnad_nrt])


def t_prop(lenghts):
    return sum(lenghts)/(2/3*3*10**8)

def ipdt(e_tocz, e_tnad_, lenghts):
    return sum(e_tocz) + sum(e_tnad_) + t_prop(lenghts)