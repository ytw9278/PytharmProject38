de1 = 'security'
de2 = 'python'
de_name1 = 'tangwei'
de_name2 = 'yuxiaobin'
age1 = '36'
age2 = '39'
d1 = '部门'
d2 = '姓名'
d3 = '年龄'

line1 = d1+':' + format(de1,'<20') + d2+':' + format(de_name1,'<20')  + d3 +':' + format(age1,'<8')
line2 = d1+':' + de2.ljust(20) + d2+':' + de_name2.ljust(20) + d3+':' + age2.ljust(10)
line3 = d1+':' + format(de1,'*<20') + d2+':' + format(de_name1,'<20')  + d3 +':' + format(age1,'<20')
# line1 = d1+':' + de1.ljust(20) + d2+':' + de_name1.ljust(20) + d3 +':' + age1.ljust(10)
# line2 = d1+':' + de2.ljust(20) + d2+':' + de_name2.ljust(20) + d3+':' + age2.ljust(10)
length = len(line1)
print('='*length)
print(line1)
print(line2)
print(line3)
print('='*length)