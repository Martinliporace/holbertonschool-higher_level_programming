#!/usr/bin/python3
num = 0
ciclo = 0

for i in range(0, 99):
    resto = i % 16
    if resto <= 15 and resto >= 10 and i <= 15:
        print(f"{i} = 0x{chr(resto + 87)}")
        if i % 15 == 0:
            ciclo += 1

    elif resto <= 15 and resto >= 10 and i > 15:
        div = i // 16
        print(f"{i} = 0x{div}{chr(resto + 87)}")
        if i % 15 == 0:
            ciclo += 1

    else:
        x = ciclo * 6
        print(f"{i} = 0x{i - x}")

    num += 1
