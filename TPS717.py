E24 = [1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5,
       8.2, 9.1]
MULTIPL = 100
R2_ar = list(map(lambda x: x * MULTIPL, E24))[9:15]  # тут меняем срез массива
# print(R2)
Vfb = 0.8
Vout_ex = 3.3
R1_ar = list(map(lambda x: x * MULTIPL / 10, E24)) + list(map(lambda x: x * MULTIPL, E24)) + list(
    map(lambda x: x * MULTIPL * 10, E24))

combinations = []

for R1 in R1_ar:
    for R2 in R2_ar:
        Vout = (R1 / R2 + 1) * Vfb
        # print(round(R1, 2), round(R2, 2), Vout)
        combinations.append({'R1': round(R1, 2), 'R2': round(R2, 2), 'dVout': abs(Vout_ex - Vout), 'Vout': Vout})

# print(combinations)
combinations_sort = sorted(combinations, key=lambda k: k['dVout'])

for i in range(3):
    print(combinations_sort[i])
# Vfb = 0.8
# print('R2', R2)
# Vout = 3.3
#
# R1 = R2 * (Vout / Vfb - 1)
# print(R1)
#
# R1 = 976
# Vout = (R1 / R2 + 1) * Vfb
# print(Vout)

# R2 = 324000
# Vout = 1
# R1 = R2 * (Vout / Vfb - 1)
# print(R1)
#
# R2 = 324000
# Vout = 1.2
# R1 = R2 * (Vout / Vfb - 1)
# print(R1)
