x = int(input())
a = [[0]*22 for i in range(22)]
a[1][1] = 1
for i in range(1,x+1):
    # print('\t'*(x-i),end='')
    for j in range(1,i+1):
        a[i][j] += a[i-1][j-1]+a[i-1][j]
        print(a[i][j],end=' ')
    print()
def Yanghui_triangle(i, j):
    if j == 1 or i == j:
        return 1
    else:
        return Yanghui_triangle(i - 1, j - 1) + Yanghui_triangle(i - 1, j)
n = int(input("please input the number of layer:"))
for i in range(1, n + 1):
    print((n - i) * '\t', end='')
    for j in range(1, i + 1):
        print("%d" % Yanghui_triangle(i, j), end='\t\t')
    print('\n')