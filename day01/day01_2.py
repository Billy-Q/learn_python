'''
**********
Date: 2021-10-26
Author: Billy-Q
**********
'''

# 定义整型变量
age = 30
# 定义浮点类型变量
score = 70.5
# 定义布尔类型变量
b = True
# 定义字符串类型变量
name = '张三'
# 获取变量类型
t = type(name)

# 定义整型变量
age = 30
# 修改成浮点类型变量
age = 70.5

itcast = '张三'
# itcast.cn = '李四'

# 下划线命名法
student_name = '张三'
# 大驼峰命名法
StudentName = '张三'
# 小驼峰命名法
studentName = '张三'

'''
数值型变量之间可以直接计算
字符串之间使用+拼接字符串
'''
str1 = 'hello'
str2 = 'world'
str3 = str1 + str2
print(str3)
'''
字符串变量和整型使用*重复拼接相同的字符串
'''
str = 'hello'
s = str*5
print(s)

'''
数值变量和字符串不能进行其它计算
str = 'hello'
a = 10
result = str+a
print(result)
'''