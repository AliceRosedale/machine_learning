import pandas as pd
b = pd.Series([9,8,7,6],index=['a','b','c','d'])

#pandas
import pandas as pd
a = pd.Series([9,'04',7,6])
print(a)

#2
s = pd.Series('04',index=['a','b','c'])
print(s)

#3
e = pd.Series({'a':9,'b':'04','c':7},index=['c','a','b','d'])
print(e)

#4
import numpy as np
m = pd.Series(np.arange(5),index=np.arange(9,4,-1))
print(m)

print(b.index)
print(b.values)

#切片
print(b[3])
print(b[:3])

#自定义索引
print(b[[
    'a','b','c'
]])


#是否在范围内
print('c' in b)
print(0 in b)



#Series自动对齐
a = pd.Series([1,4,3],['c','d','e'])
b = pd.Series([9,4,7,6],['a','b','c','d'])
a+b

b['a'] = 15
print(b)

b[['a','c']] = 20
print(b)

b.drop('a')
print(b)

#DataFrame二维数据
d = pd.DataFrame(np.arange(10).reshape(2,5))
print(d)

#ndarray对象字典创建
dt = {
    'one':pd.Series([1,2,3],index=['a','b','c']),
    'two':pd.Series([9,4,7,6],index=['a','b','c','d'])
}
d = pd.DataFrame(dt)
print(d)

d1 = {
    '城市':['北京','上海','广州','深圳','沈阳'],
    '环比':[4,123,555,666,101],
    '同比':[7777,123,111,156,101],
    '定基':[156,123,32,666,101],
}
d = pd.DataFrame(d1,index=['c1','c2','c3','c4','c5'])
print(d)

print(d.index)
print(d.columns)
print(d.values)

#找其中一列或者一行
print(d['同比'])
print(d.loc['c2'])

#重新索引
print(d.reindex(index=['c5','c4','c3','c2','c1']))
print(d.reindex(columns=['城市','环比','同比','定基']))

newc = d.columns.insert(4,'新增')
newd = d.reindex(columns=newc,fill_value=4)
print(newd)

print(d.drop('c5'))
print(d.drop('同比',axis=1))