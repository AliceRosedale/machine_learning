
def dfs(n):
    if n >x:
        for i in range(1,x+1):
            print('%5d'%ans[i],end='')
        print()
        return
    for i in range(1,x+1):
        if visited[i]==0:
            visited[i]=1    #保存现场
            ans[n] = i      #更新答案
            dfs(n+1)        #继续把后面的数放入数组
            visited[i]=0    #释放现场


if __name__ == '__main__':
    x = int(input())
    ans = [0 for _ in range(x+1)]
    visited = [0 for _ in range(x+1)]
    dfs(1)