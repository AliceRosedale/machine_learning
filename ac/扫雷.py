n,m = map(int,input().split(' '))
a = [[0]*(m+2) for _ in range(n+2)]
b = [[i for i in input()] for _ in range(n)]
for i in range(1,n+1):
    for j in range(1,m+1):
        # if b[i][j]=='*':
        a[i][j]=b[i-1][j-1]
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i][j]=='*':
            print(a[i][j],end='')
            continue
        count = 0
        x=i
        y=j
        for xx,yy in [(-1,-1),(-1,0),(-1,1),(0,1),(0,-1),(1,-1),(1,0),(1,1)]:
            if a[x+xx][y+yy]=='*':count+=1
        print(count,end='')
    print()

# n,m = map(int,input().split(' '))
# a = [[0]*(m+2) for _ in range(n+2)]
# b = [[i for i in input()] for _ in range(n)]
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         a[i][j]=b[i-1][j-1]
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         count = 0
#         if a[i][j]=='*':
#             print(a[i][j],end='')
#             continue
#         else:
#             if a[i][j+1]=='*':count+=1#右
#             if a[i][j-1]=='*':count+=1#左
#             if a[i-1][j]=='*':count+=1#上
#             if a[i+1][j]=='*':count+=1#下
#             if a[i-1][j-1]=='*':count+=1#坐上
#             if a[i-1][j+1]=='*':count+=1#右上
#             if a[i+1][j+1]=='*':count+=1##左下
#             if a[i+1][j-1]=='*':count+=1
#             print(count,end='')
#     print()