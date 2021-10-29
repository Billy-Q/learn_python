'''
**********
Date: 2021-10-26
Author: Billy-Q
**********
'''

# 直接输出数据
print(10)
name = '张三'
# 输出变量
print(name)
# 输出多个数据和变量
print(10, name)

# 输入年纪
age = input('请输入年纪')
print(age)
# 获取age类型
t = type(age)
print(t)

# 输入整型变量a
a = int(input('请输入第一个数'))
# 输入整型变量b
b = int(input('请输入第二个数'))
# 输出a+b的结果
print(a+b)

price = float(input('请输入苹果单价'))
weight = float(input('请输入苹果重量'))
money = price*weight
print('付款金额:%.2f'%money)

# 打印名片
name = input('请输入姓名:')
com = input('请输入公司名:')
title = input('请输入职务:')
telephone = input('请输入电话号码:')
email = input('请输入邮箱:')

# 输入50个*
print('*'*50)
# 公司名称
print('公司名称:%s'%com)
# 输出空行
print()
# 姓名(职位)
print('%s(%s)'%(name,title))
print()
print('电话:%s'%telephone)
print('邮箱:%s'%email)
print('*'*50)
