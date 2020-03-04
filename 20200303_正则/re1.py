import re

msg = '<h1>11111</h1>'
pattern = r'<.+>(.*)</.+>'
result = re.match(pattern, msg)
print(result.group())

# number
msg1 = '<h1>2222</h1>'
pattern1 = r'<(.+)>(.*)</\1>'  # \1表示引用分组内容
print(re.match(pattern1, msg1))
print(re.match(pattern, msg))

# 起名的方式 (?P<名字>pattern) (?P=名字)
msg2 = '<html><h1>333<h1><html>'
pattern2 = r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)<(?P=name2)><(?P=name1)>'
print(re.match(pattern2, msg2))

'''
re模块
match 从开头匹配一次
search  只匹配一次
findall 查找所有
sub(pattern,'新内容' | func，string)
split(pattern,string) 分成列表

基础：
.
[]
|
()

量词：
*
+
?
{m}
{m,n} 前后都包含

预定义：
\s  space
\d  digit
\w  word
\b  边界
\大写字母 反向范围


贪婪：
python中数量词默认是贪婪的，即总是尝试匹配尽可能多的字符

在 * ,?,+,{m,n} 后面加?,使贪婪变非贪婪
'''

# sub
string = 'java:100,python:1000'
print(re.sub('\d+', '90', string))


def func(temp):
    num = temp.group()
    return str(int(num) + 1)


print(re.sub(r'\d+', func, string))

# split
print(re.split(r'[,:]', string))

# 贪婪
msg45 = 'abc123abc'
pattern4 = r'abc(\d+)'  # 贪婪
pattern5 = r'abc(\d+?)'  # 非贪婪

print(re.match(pattern4, msg45))
print(re.match(pattern5, msg45))
