#dictionary 字典
#列表 或 元组 可以转化为字典，但必须成对儿出现
d1 = dict([[1,2],[3,4]])
d2 = dict(([1,2],[3,4]))
d3 = dict(((1,2),[3,4]))
d4 = dict([(1,2),[3,4]])

print(d1,d2,d3,d4)

#增改
# d1[key] = value

#get(key)  不存在 返回None
#get(key,default)  存在-->返回值，不存在-->返回default

d1.get(1)
d1.get(5,100)

#items() | keys() | values()

#内置函数 
    #删除 pop(key[,default]) 删除key,返回value值  若不存在key,返回value
    #popitem()随机删除(一般从末尾删除)
    #clear()
v1 = d1.pop(1) #2 并删除1

    #update()  合并操作(存在则更改)
    #fromkeys(seq)
lst = [1,2,3]
print(dict.fromkeys(lst))
print(dict.fromkeys(lst,10))
