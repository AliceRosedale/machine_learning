'''
砝码1：    1
砝码两个砝码1，4：      1，3，4，5
拿到砝码6 ： 1，3，4，5，6，7，9，10，11，2，3，2，1（不用发码6就有1，3，4，5组合）
使用set消除重复元素
'''

n = int(input())
a= [int(i) for i in input().split(' ')]
weight = set()
weight.add(0)
for i,num in enumerate(a):
    list_a = list(weight)
    for j in list_a:
        weight.add(num+j)
        weight.add(abs(num-j))

print(len(weight)-1)