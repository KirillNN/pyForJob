Vinmax = 28.8
Vout = 1.2
f = 500000  # 250-600 кГц
dI = 0.3
Imax = 24 / 0.95
Imaxph = Imax / 3
L = (Vout / (f * dI * Imaxph)) * (1 - Vout / Vinmax)
print(f'Не менее {L * 1000000:.2f} мкГн')

Rsense = 0.065 / (Imaxph * (1 + 0.34 / 2))  # p.21
print(f'Не более {Rsense * 1000:.2f} мОм')
Rsense = 3 * 0.05 / Imax  # p.16
print(f'Не более {Rsense * 1000:.2f} мОм')

# The IC works well with values of RSENSE from 0.002Ω to 0.02Ω.
