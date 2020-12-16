# # s = 'fuck tangwei'
# # s = s.replace('tangwei', 'yuxiaobin')
# #
# # print(s)
# # rint(le)
# #
# # age = input('你几岁了？')
# # print(age)
# # print(type(age))
# # length = len(s)
# # print(length)
#
# # bank = 1000
# # money = input('请输入金额:')
# # money = int(money)
# # if money <= bank :
# #     bank = bank-money
# #     print('取款成功，余额为:'+ str(bank))
# # else:
# #     print('取款失败，当前余额为:'+ str(bank))
#
#
#
#
#
# # for i in range(1,101):    #左开右关  遍历
# #     print(i)
#
# #
# # for ch in 'Python':
# #     print(ch)
#
# # a = 1
# # while a <= 1000:
# #     print(a)
# #     a = a+1
#
#
# # while True:
# #     answer = input('你的腿怎么样？能坚持吗？')
# #     if answer=="y":
# #         print('加油!')
# #     else:
# #         print('不能，退赛！')
# #         break
#
#
# # circle = 0
# # for i in range(1, 12):
# #     answer = input('能跑吗？')
# #     if answer != 'y':
# #         continue
# #     circle+=1
# # print('一共跑了', circle, '圈')
#
#
# lst = [50, 51, 52, 53, 54]
# # print(lst)
# # print(lst[3])
# # print(lst[-2])
# # lst.append(100)
# # print(lst)
# # lst[1]=88
# # print(lst)
# # lst.remove(54)
# # print(lst)
# # for i in range(0, len(lst)):
# #     print(lst[i])
# # for item in lst:
# #     print(item)
#
# # lst = [50, 51, 52, 53, 54]
# # lst1 = lst[1:]
# # lst2 = lst[1:3]
# # print(lst1)
# # print(lst2)
#
# dic = {'41': 10, '42': 11, '43': 12}
# print(dic)
# print(dic['42'])
# dic['45'] = 100 #添加元素
# dic['45'] = 10
# print(dic)
# # del dic['43']  # 删除元素
# print(dic)
#
# for i in dic:   #遍历打印
#     print(i, dic[i])
#
# #集合，单身没有妻子，只有老公，而字典是有老公有妻子
# dicc = {'41', '42', '43'}
# print(dicc)
# dicc.add('34')
# print(dicc)
# dicc.remove('42')
# print(dicc)
# for i in dicc:
#     print(i)
# lst = list(dicc) #集合转成列表
# print(lst[0])



# def fun(x):
#     print(int(x/10))
#
# fun(10)
# fun(20)

# def cacl(a, b):
#     return a+b
# x = cacl(10, 20)
# y = cacl(20, 30)
#
# print(x)
# print(y)


# class Girl:
#     def __init__(self, hair, name, age):
#         self.hair = hair
#         self.name = name
#         self.age = age
#     def eat(self):
#         print(self.name, '我想入肉你')
#
#
# girl1 = Girl('长头发','tt', 36)
# girl1.eat()
# girl2 = Girl('短头发','yxb', 39)
# girl2.eat()


# class Car:
#     def __init__(self, color, brand, type):
#         self.color = color
#         self.brand = brand
#         self.type = type
#     def run(self):
#         print(self.color, '颜色的小汽车在行驶')
#         print('This is a', self.type, 'car')
# car1 = Car('white', 'BWM', 'X5')
# car1.run()


import openpyxl
