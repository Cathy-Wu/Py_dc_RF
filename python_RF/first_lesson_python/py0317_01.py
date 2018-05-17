#coding:utf-8
# def f1(x):
#     return x+2     #定义函数返回值
# print('f1=',f1(77))  #调用（call）函数f1,1是实际参数


#带多个函数的参数以及变量的作用范围
# c=100                   #这里的c是全局变量（global）
# a=500                   #这里的a是全局变量（global）
# def f2(x,y):            #x,y是两个参数
#     a=300               #这个a是局部变量(local)
#     c= x**3+y**2+a  #c是一个局部变量
#     return c
# print('c=',f2(3,4))
# print(f2)
# a=type(f2)
# print(a)

# def f3(x,y=4):            #y默认等于4
#     a=300
#     c= x**3+y**2+a
#     import math
#     print (math.sqrt(c))
# print('cc=',f3(3))
#

# def Man(name,age=16):
#     if name=='Cathy':
#         return ('%s is %d years old'%(name,age))
#     else:
#         return 'he is a boy'
# print(Man('Cathy',20))



#if .....else.....
# def Man(name,age):
#     a=input('plz input the sex:')
#     if a=='girl':
#         if age==20:
#             return ('%s is %d years old'%(name,age))
#         else:
#             return ('%s is %d years older,It is too old !'%(name,age))
#     elif a=='boy':
#         return 'he is a boy'
#     else:
#         return'i can not define!'
#
# a=Man('cathy',22)
# print(a)

def f(x):
    if x>0 and x<10:
        return ('ok')
    elif x>5:
        print('pok')
    else:
        print('nokk')
        x=x+100
        x*1000
    return 'OK!!!'
tmp=f(5)
print(tmp)
print('dddone')
    
    









