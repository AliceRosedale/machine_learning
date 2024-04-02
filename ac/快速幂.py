def fast(a,b,c):
    ans = 1
    a =a%c
    while b:
        if b % 2 ==1:
            ans = (ans*a)%c
        a = (a*a)%c
        b //=2
    return ans
a,b,p = map(int,input().split(' '))
s = fast(a,b,p)
print(f'{a}^{b} mod {p}={s}')

#使用位运算改进
def fast(a,b,c):
    ans = 1
    a =a%c
    while b:
        if b & 1:   #通过与1做与运算判断奇偶，0为偶
            ans = (ans*a)%c
        a = (a*a)%c
        b >>1   #二进制中整除2相当于整体右移动一位
    return ans
a,b,p = map(int,input().split(' '))
s = fast(a,b,p)
print(s)