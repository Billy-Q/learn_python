'''
**********
Date: 2021-10-28
Author: Billy-Q
**********
'''

# 1.我们出拳   定义变量保存用户输入
my = int(input('请输入出拳'))
# 2.电脑随机出拳（假定电脑出石头）
com = 1
# 3.判断胜负
if (my==1 and com==2) or (my==2 and com==3) or (my==3 and com==1):
    # 用户胜利
    print('用户胜利, my=%d,com=%d'%(my,com))
elif my==com:
    print('平局，决战到天亮')
else:
    print('电脑胜利,my=%d,com=%d'%(my,com))

# python生成随机数 random
import random
# 1.我们出拳   定义变量保存用户输入
my = int(input('请输入出拳:'))
# 2.电脑随机出拳(假定电脑出石头)
# 指定开始 结束 包含开始包含结束
com = random.randint(1,3)
# 3.判断胜负
if (my==1 and com==2) or (my==2 and com==3) or (my==3 and com==1):
    # 用户胜利
    print('用户胜利,my=%d,com=%d'%(my,com))
elif my==com:
    print('平局，决战到天亮,my=%d,com=%d'%(my,com))
else:
    print('电脑胜利,my=%d,com=%d'%(my,com))