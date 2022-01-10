Iomax = 10
fSW = 500000
Vinmax = 28.8
Vout = 1.2

Lx = (3/(Iomax*fSW))*((Vinmax-Vout)*Vout/Vinmax)

# print(Lx)
print(f'Индуктивность равна {Lx*1000000} мкГн')