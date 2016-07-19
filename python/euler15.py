
paths = [[0 for m in range(21)] for n in range(21)]

for n in range(0,21):
    for m in range(0,21):
        paths[n][m] = 1 if (n == 0 or m == 0) else paths[n-1][m] + paths[n][m-1]

print(paths[20][20])
