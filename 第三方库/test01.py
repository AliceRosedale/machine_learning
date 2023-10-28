# a = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print([item2 for item1 in a for item2 in item1 if item2 % 2 ==0])
#
#质数
# prime_numbers = [num for num in range(2, 101) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
# print(prime_numbers)
#法二
# num=[]
# i=2
# for i in range(2,100):
#    j=2
#    for j in range(2,i):
#       if(i%j==0):
#          break
#    else:
#       num.append(i)
# print(num)
# a = [[1, 2, 3, 4, 5],
#      [6, 7, 8, 9, 10],
#      [11, 12, 13, 14, 15],
#      [16, 17, 18, 19, 20],
#      [21, 22, 23, 24, 25]]
#
# b = [a[i][i] for i in range(5)]
# print(b)
#
# a = [2]
# for b in range(3, 101):
#     for c in range(2, int(b**0.5) + 1):
#         if b % c == 0:
#             break
#     else:
#         a.append(b)
#
# print(a)
#
# A = [1, 2, 3, 4, 5]
# b = "abcde"
# a = {}
# for i in range(len(A)):
#     a[A[i]] = b[i]
# print(a)
# #遍历列表
# b=[[i+1,i+2,i+3] for i in [0,3,6]]
# print(b)

# a = [[1, 2, 3, 4, 5],
#      [6, 7, 8, 9, 10],
#      [11, 12, 13, 14, 15],
#      [16, 17, 18, 19, 20],
#      [21, 22, 23, 24, 25]]
# s = [i for i in a ]
# print(s)
# print(a)
print('34' in '1234')

a = '1234'
b = [1,2,4,3]
