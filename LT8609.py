E24 = [1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5,
       8.2, 9.1, 10]

E96 = [1.00, 1.02, 1.05, 1.07, 1.10, 1.13, 1.15, 1.18, 1.21, 1.24, 1.27, 1.30, 1.33, 1.37, 1.40, 1.43, 1.47, 1.50, 1.54,
       1.58, 1.62, 1.65, 1.69, 1.74, 1.78, 1.82, 1.87, 1.91, 1.96, 2.00, 2.05, 2.10, 2.15, 2.21, 2.26, 2.32, 2.37, 2.43,
       2.49, 2.55, 2.61, 2.67, 2.74, 2.80, 2.87, 2.94, 3.01, 3.09, 3.16, 3.24, 3.32, 3.40, 3.48, 3.57, 3.65, 3.74, 3.83,
       3.92, 4.02, 4.12, 4.22, 4.32, 4.42, 4.53, 4.64, 4.75, 4.87, 4.99, 5.11, 5.23, 5.36, 5.49, 5.62, 5.76, 5.90, 6.04,
       6.19, 6.34, 6.49, 6.65, 6.81, 6.98, 7.15, 7.32, 7.50, 7.68, 7.87, 8.06, 8.25, 8.45, 8.66, 8.87, 9.09, 9.31, 9.53,
       9.76, 10]


def remove_value(list, value):
    for item in value:
        list.remove(item)


E24_E96 = sorted(E24 + E96)
# print(E24_E96)

# print(E24_E96)


# -------------- входные данные --------------------
V = 5  # задаем выходное напряжение
print_count = 20  # количество выводимвых значений
# -------------- входные данные --------------------


# remove_value(E24_E96_slice, [8.2,5.6,3.9,4.42,5.1,5.23]) # удаляем лишние значения

E24_E96_slice_R1 = [i for i in E24_E96 if i >= 8.2]
print('R1', E24_E96_slice_R1)
E24_E96_slice_R2 = E24_E96[:]
print('R2', E24_E96_slice_R2)

combinations = []

for R2 in E24_E96_slice_R2:
    R2 *= 100
    for R1 in E24_E96_slice_R1:
        R1 *= 100
        Vout = 0.782 * (R1 / R2 + 1)
        combinations.append(
            {'R1': round(R1, 2), 'R2': round(R2, 2), 'dVout': abs(V - Vout), 'Vout': Vout,
             'error (%)': round(100 * abs(V - Vout) / V, 2)})
        # print(f'R1 = {R1} кОм', f'R2 = {R2} кОм', f'Vout = {Vout:.2f} В')
        # print(f'Vout = {Vout:.2f} В')

combinations_sort = sorted(combinations, key=lambda k: k['dVout'])
for i in range(print_count):
    print(combinations_sort[i])

# Vout = 0.782 * (R1 / R2 + 1)
# print(Vout)

# for i in E96:


# MULTIPL = 100
# R2_ar = list(map(lambda x: x * MULTIPL, E24))[9:15]  # тут меняем срез массива
# # print(R2)
# Vfb = 0.8
# Vout_ex = 3.3
# R1_ar = list(map(lambda x: x * MULTIPL / 10, E24)) + list(map(lambda x: x * MULTIPL, E24)) + list(
#     map(lambda x: x * MULTIPL * 10, E24))
#
# combinations = []
#
# for R1 in R1_ar:
#     for R2 in R2_ar:
#         Vout = (R1 / R2 + 1) * Vfb
#         # print(round(R1, 2), round(R2, 2), Vout)
#         combinations.append({'R1': round(R1, 2), 'R2': round(R2, 2), 'dVout': abs(Vout_ex - Vout), 'Vout': Vout})
#
# # print(combinations)
# combinations_sort = sorted(combinations, key=lambda k: k['dVout'])
#
# for i in range(3):
#     print(combinations_sort[i])
# # Vfb = 0.8
# # print('R2', R2)
# # Vout = 3.3
# #
# # R1 = R2 * (Vout / Vfb - 1)
# # print(R1)
# #
# # R1 = 976
# # Vout = (R1 / R2 + 1) * Vfb
# # print(Vout)
#
# # R2 = 324000
# # Vout = 1
# # R1 = R2 * (Vout / Vfb - 1)
# # print(R1)
# #
# # R2 = 324000
# # Vout = 1.2
# R1 = R2 * (Vout / Vfb - 1)
# print(R1)
