# можно делать конфигурацию из 1, 2, 3 препрегов суммарно

need_um = int(input('Введите требуемую толщину в мкм: '))

need_um_stack_min = []
need_um_stack_max = []
min_um = 0
min_um_lvl1 = 1
max_um = 10000
max_um_lvl1 = 100000

prepreg_1 = [0, 51, 76, 125, 190]  # в микронах
prepreg_2 = [0, 51, 76, 125, 190]  # в микронах
prepreg_3 = [0, 51, 76, 125, 190]  # в микронах

for item_1 in prepreg_1:
    for item_2 in prepreg_2:
        for item_3 in prepreg_3:
            sum_um = item_1 + item_2 + item_3
            if min_um < sum_um <= need_um:
                if min_um_lvl1 != min_um:
                    min_um_lvl1 = min_um
                    need_um_stack_min_lvl1 = need_um_stack_min
                min_um = sum_um
                need_um_stack_min = [item_1, item_2, item_3]
            if need_um <= sum_um < max_um:
                if max_um_lvl1 != max_um:
                    max_um_lvl1 = max_um
                    need_um_stack_max_lvl1 = need_um_stack_max
                max_um = sum_um
                need_um_stack_max = [item_1, item_2, item_3]

print(min_um, need_um_stack_min, max_um, need_um_stack_max)
print(min_um_lvl1, need_um_stack_min_lvl1, max_um_lvl1, need_um_stack_max_lvl1)
