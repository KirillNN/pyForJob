import math

eps_exelent = 1 * 10 ** -13  # заданная относительная точность
eps = 1 * 10 ** -13  # заданная точность
half_pi = 1.57079632679489661923132
a = -1  # нижняя граница
b = 1  # верхняя граница
<<<<<<< Updated upstream
dop = 0.05
h2 = 0.25
n = math.ceil((b - a) / eps ** 0.25 / 4) * 4  # число шагов
=======
h2 = 0.25
n = math.ceil((b - a) / eps ** 0.25 / 4) * 4*2048  # число шагов


def sympson(f, a, b, n):
    h = (b - a) / n
    summ = f(a) + f(b)
    for i in range(1, n):
        # if i % 1000000 ==0:
        #     print(i)
        k = 2 + 2 * (i % 2)
        summ += k * f(a + i * h)
    summ *= h / 3
    return summ

>>>>>>> Stashed changes


def sympson(f, a, b, n):
    h = (b - a) / n
    summ = f(a) + f(b)
    for i in range(1, int(n)):
        # if i % 1000000 ==0:
        #     print(i)
        k = 2 + 2 * (i % 2)
        summ += k * f(a + i * h)
    summ *= h / 3
    return summ


<<<<<<< Updated upstream
=======
def function(x):
    return (1 - x ** 2) ** 0.5
    # return math.sin(x)
>>>>>>> Stashed changes

def function(x):
    return (1 - x ** 2) ** 0.5
    # return 16*x**4-12*x**2+1
    # return 64 * x ** 6 - 80 * x ** 4 + 24*x**2-1

# n=1024

for i in range(1,12):
    res1 = sympson(function, a, b, n)
    res2 = sympson(function, a, b, n / 2)
    print('При n =',n, 'получаем относительную точность', abs((res1-res2)/res2))
    print('Значение интеграла:', res1)
    # print(abs((res1-res2)/res1))
    n *= 2

# print(half_pi)
# print(res1, res2, abs((res1-res2)/res2))
# res1 = sympson(function, a, b, n)
# res2 = sympson(function, a, b, n/2)
# print('При n =',n, 'получам точность', abs((res1-res2)/res2))


#
# def simpson(f, a, b, n):
#     h = (b - a) / n  # шаг
#     k = 0.0
#     x = a + h
#     for i in range(1, int(n / 2) + 1):
#         k += 4 * f(x)
#         x += 2 * h
#
#     x = a + 2 * h
#     for i in range(1, int(n / 2)):
#         k += 2 * f(x)
#         x += 2 * h
#     return (h / 3) * (f(a) + f(b) + k)

<<<<<<< Updated upstream
=======
n = int(2**16)

dopusk = 0.001

res1 = sympson(function, a+dopusk, b-dopusk, n)
res2 = sympson(function, a+dopusk, b-dopusk, n*2)

print(half_pi)
# print(res, n, res - half_pi)
print(res1, res2, (res2 - res1) / res2)
# print(sympson(function, 1, 2, 10))

# 1.5707932690635178 3560 -3.0577313787638616e-06
# 1.5707952457367587 7120 -1.0810581378972728e-06

>>>>>>> Stashed changes

# 1.5707963267948966
# 1.5707963266461233 5000001 -1.4877321596884485e-10
# 1.5707963267742837 10000002 -2.0612844764400506e-11
# 1.5707963267761502 20000001 -1.8746337815400693e-11
# 1.5707963267876968 20000000 -7.19979631469414e-12
# 1.5707963267945009 200000000 -3.956834859764058e-13
# 1.5707963267952412 300000000 3.446132268436486e-13
<<<<<<< Updated upstream
# 1.5707963267967522 500000000 1.8556267633584866e-12
# 1.5707963268863356 10000000000 9.143907853115252e-11
=======
>>>>>>> Stashed changes
