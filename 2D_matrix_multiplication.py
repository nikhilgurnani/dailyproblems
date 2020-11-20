def multiply(a,b,n):
    c = [[0,0],
         [0,0]]
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                c[i][j] += a[i][k] * b[k][j]
    return c

print(multiply([[2, 1], [1,2]], [[3,4],[1,2]], 2))