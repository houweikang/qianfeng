#小整数对象池 [-5,256]
#intern机制处理空格一个单词的复用机会大，所以创建一次，有空格创建多次，但是字符串长度大于20，就不是创建一次了。
#test

str_1 = 'hello world'
print(str_1[:5:-1])
print(str_1[:5])
print(str_1[::-1])
print(str_1[-7:-10:-1])
print(str_1[::-2])

str_1 = 'hwk is handsome '
#capitalize() 首字母大写
print(str_1.capitalize())

#istitle,title
print(str_1.istitle())
print(str_1.title())

#upper isupper 
#lower islower
#find rfind lfind
#replace(old,new[,max])

# encode 编码 decode 解码
msg = '哈哈！'
msg_encode = msg.encode('utf-8')
print(msg_encode)
msg_decode = msg_encode.decode('utf-8')
print(msg_decode)

# endwith startswith --->True False
print(r'\a')

#isalpha 字母 isdigit 数字
list_1 = [1,2,3,4,5,6]
a = list_1[:2:-1]
print(a)

#join

x='abc'
y = 'def'
z = ['d','e','f']
print(x.join(y),'------------',x.join(z))