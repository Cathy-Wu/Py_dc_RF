#coding:utf-8
#列表 list

# l1=[ ]                          #空列表
# l2=[1,2,'a','china']       #有4个元素的列表
# print(len(l2))                #len-length,求列表长度
# print(l2[0],l2[len(l2)-1],l2[-1])   #len(l2)-1,这个是传统的求最后以为元素的做法
# l2[2]='武汉'
# print(l2)
# l1=[ ]                                            #空列表

# l2=[1,2,'a','china',2,'china','china']                         #有4个元素的列表
#
# print(len(l2))                                  #len-length,求列表长度
# # print('l2:',l2[0],l2[len(l2)-1],l2[-1])   #len(l2)-1,这个是传统的求最后以为元素的做法
# l2[2]='武汉'                                   #列表中的元素可以被修改
# print(l2)
# l4=['门道','好的']
# l2.append(l4)               #append 属于l2列表对象的方法,追加
# print('l2=',l2)
#
# l3=l2.copy()
# print('l3=',l3)
#
# a=l3.pop(2)           #pop,remove and return item at index (default last).
# print(a)
# print(l3)
#
# l1=[1,12,'cathy']
# # extend 属于拓展
# l3.extend(l1)
# print('l3=',l3)
#
# #insert:insert object before index
# l1=[1,12,'cathy']
# l3.insert(0,l1)
# print('l3=',l3)
#
# #remove, remove first occurrence of value.
# l3.remove(['门道', '好的'])
# print('l3=',l3)
#
# #reverse, L.reverse()
# l3.reverse()
# print('l3=',l3)
#
# # sort 排序，返回None
# l4=[2,7,3,1,0,55,22,10,5]
# l4.sort(key=None,reverse=True)
# print('l33=',l4)

#元组 tuple,元组不能修改,只有计数和索引
# t=(3,2,1,3,3,3,6,7,1,33,3,)
# print('t[3]=',t.count(3))   #count,计算某种元素的个数
# print(t[0],t[-1],len(t))    #index,索引
#
# t=(4,)
# print(type(t))
# print(type(t) is tuple)

#切片
# l=[1,2,3,4,5]
# print(l[1:4])

# l=[1,2,3,4,5]
# print(id(l))
# l11=l                       #传的是一种引用，地址也会相应的改变
# print(id(l11))
# print('l11=',l11)
# l11.append('77')
# print(l11)
# print(id(l11))
# print(l)
# print(id(l))

# l=[1,2,3,4,5]
# l22=l.copy()
# print('l22=',id(l22))
# print('l22=',l22)      #只是完完全全的copy,与切片[:]一样，开辟了另一个地址空间
# l22.append('8')
# print(l22)
# print(id(l22))
# print(l)
# print(id(l))

# s='123456'
# print(s[0],s[1:4])

# t=(1,2,3,4,5,6)
# print(t[1:4])
# print(t[::-2])

#10的阶层
# total=1
# for i in range(1,10):
#     total=total*i
#     print(i,total,end='\n')
    
#100以内的所有偶数相加
# total=0
# for i in range(0,101,2):
#     total=total+i
#     print(i,end=' ')
# print('\n','所有的偶数和是:%s'%total)       #也可以在句首换行
  
##100以内的所有奇数相加
#total=0
#for i in range(1,100,2):
    #total=total+i
    #print(i,end=' ')
#print('\n','所有的奇数和是:%s'%total)

# t1=t2=0
# for i in range(1,101):
#     if i%2==0:
#         t1=t1+i
#     else:
#         t2=t2+i
# print("所有的偶数和是：%s \n所有的奇数和是：%s"%(t1,t2))

#创建100以内的10个随机数       
# l=[]
# for i in range(1,10):
#     import random
#     x=random.randint(1,101)
#     l.append(x)
#     # print(l)
# print(l)

#while 循环
# total=0
# i=0
# while i<101:
#     total = total+i
#     i=i+1
# print('i=%s,total=%s'%(i,total))
    
    
# total=0
# i=0
# while i<10:
#     i=i+1
#     total = total+i
#     if i==5:
#         break                #中断循环
#     print('i=%s,total=%s'%(i,total))
# print('ii=%s,totall=%s'%(i,total))

    
# total=0
# i=0
# while i<10:
#     total = total+i
#     i=i+1
#     if i>=5:
#         continue               #继续循环
#     print('i=%s,total=%s'%(i,total))
# print('ii=%s,totall=%s'%(i,total))


#for i in range(1,10):
    #if i>=5:
        #continue
    #print('i=',i)
#print(i)

#for i in range(1,10):
    #if i>=5:
        #break
    #print('i=%s'%i)
#print(i)

#字典 查询速度很快
'''d={} #定义了一个变量，值是空字典
d1={'china':'中国，祖国',
    'USA':'你好',
    'Japan':'樱花'}   #'china':'中国，祖国'，叫做条目items

print(d1['USA'])     #获取字典的方式1
#print(d1.get('china'))  #获取字典的方式2
#print(d1.items())
#print(d1.keys())
#print(d1.values())
##print(d1.popitem())
##c=d1.pop('china')
##print('c=',c)
#print(d1)

#把字典转换成列表
print(list(d1.keys()))

c=d1.copy()
print(c)

#a={1:2}
#c.update(a)
#print('c=',c)


#字典和for 常见用法搭配
#for i in d1:
    #print(i,d1[i])
    
#for k,v in d1.items():
    #print(k,v)

#print(d1.fromkeys(range(1,3),'cathy'))

#ss=d1.get('china1')
#print('ss==',ss)
#s=d1.setdefault('china1','ddsd')
#print('s=',s)
    

#嵌套a访问
j=[
    {'name':{'age':'20'}},
    {'family':['baba','mama','jiejie']},
     ['abby','jason','cook']
]
#print(j[3][3]['job'])
#print(j[2][1])
#print(j[0]['name']['age'])
print(j,type(j))
print(str(j),type(str(j)))
a=tuple(j)
print(a,type(tuple(j)))



#print(j,type(dict(j)))

#print(dict(j))
#print(type(j))'''


import json
json.loads
j='''{"a":"aa","b":[{"c":"cc","d":"dd"},{"f":{"e":"ee"}}]}'''
d=json.loads(j)
dd={}


def extdict(src):
    if isinstance(src,list):
        for i in src:
            extdict(i)
    else:
        for i in src.keys():
            if isinstance(src[i],list) or isinstance(src[i],dict):
                extdict(src[i])
            else:
                dd[i]=src[i]
extdict(d)
print(dd)







