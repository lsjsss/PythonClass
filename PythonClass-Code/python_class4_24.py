
for i in range(-4, 5):
    if i < 0: j = -i
    else: j = i
    print(str((''*j + '*' * (9 - 2 * j)).center(20)))
