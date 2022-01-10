def dw2float(dw_array):
    assert (len(dw_array) == 4)
    dw = int.from_bytes(dw_array, byteorder='little', signed=False)
    s = -1 if (dw >> 31) == 1 \
        else 1  # Знак
    e = (dw >> 23) & 0xFF;  # Порядок
    m = ((dw & 0x7FFFFF) | 0x800000) if e != 0 \
        else ((dw & 0x7FFFFF) << 1)  # Мантисса
    m1 = m * (2 ** (-23))  # Мантисса в float
    return s * m1 * (2 ** (e - 127))


def float_read(sign, order, mantissa):
    if len(sign) != 1:
        return f'sign length wrong: need 1, has {len(sign)}'
    if len(order) != 8:
        return f'order length wrong: need 8, has {len(order)}'
    if len(mantissa) != 23:
        return f'mantissa length wrong: need 23, has {len(mantissa)}'
    order_dec = 0
    for i in range(len(order)):
        # print(order[len(order)-1-i])
        order_dec += int(order[len(order) - 1 - i]) * 2 ** i
    order_dec -= 127
    find_right_one = mantissa.rfind('1')
    new_mantissa = f'1{mantissa[0:find_right_one + 1]}'
    new_mantissa_dec = 0
    for i in range(len(new_mantissa)):
        # print(order[len(order)-1-i])
        new_mantissa_dec += int(new_mantissa[len(new_mantissa) - 1 - i]) * 2 ** i

    result = new_mantissa_dec * 2 ** (order_dec - find_right_one - 1)

    return order_dec, find_right_one, new_mantissa, new_mantissa_dec, result


def bin_to_hex_ar(sign, order, mantissa) -> list | None:
    if len(sign) != 1:
        print(f'sign length wrong: need 1, has {len(sign)}')
        return None
    if len(order) != 8:
        print(f'order length wrong: need 8, has {len(order)}')
        return None
    if len(mantissa) != 23:
        print(f'mantissa length wrong: need 23, has {len(mantissa)}')
        return None
    all_sig = sign + order + mantissa
    dig3 = hex(int(all_sig[0:7], 2))
    dig2 = hex(int(all_sig[8:15], 2))
    dig1 = hex(int(all_sig[16:23], 2))
    dig0 = hex(int(all_sig[24:31], 2))
    print([dig3, dig2, dig1, dig0])
    return [int(dig0,16), int(dig1,16), int(dig2,16), int(dig3,16)]


fl_one = float_read('0', '01111111', '00000000000000000000001')
print(fl_one)
fl_one = dw2float(bin_to_hex_ar('0', '01111111', '00000000000000000000001'))
print(fl_one)
# fl_one = float_read('0', '01111100', '01000000000000000000000')
# print(fl_one)
# fl_one = float_read('0', '01111100', '11000000000000000000000')
# print(fl_one)


# fl_one = float_read('0', '11111110', '11111111111111111111111')
# print(fl_one)
# fl_one = float_read('1', '00000000', '11111111111111111111111')
# print(fl_one)
# fl_one = float_read('1', '00000000', '11111111111111111111110')
# print(fl_one)


# print(dw2float([0xFF, 0xFF, 0x7F, 0x7F]))
