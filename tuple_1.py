#只含一个元素 要加逗号
tuple_1 = (1,) # 非 tuple_1 = (1)
#不能增删改，只能查 下标，切片


t1 = (1,2,3,4,5,6)

#函数：
max()
min()
len()
sum()
#sorted ----> 返回列表
l2 = tuple(sorted(l1))
    #自带函数
    # index() 
    # count()

# *的用法   拆包  装包

a,*b,c = t1
print(a,b,c)

l1 = list(t1)
a,*b,c = l1
print(a,b,c)

#元组 符号
# +
# *
# in  | not in
# is  | not


