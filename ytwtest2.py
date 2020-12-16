# import os
# print(os.getcwd())  #存放的文件夹
# print(os.path.join('e:\\officepython', 'chap2'))
# print(os.listdir())
# lst = os.listdir()
# for i in lst:
#     print(i, type(i), len(i)) #类型，长度

# lst2 = os.listdir('.')
# for i in lst2:
#     print(i, len(i))

# lst = os.scandir()
# for i in lst:
#     # print(i, type(i), i.name, i.path, i.is_dir())
#     print(i.name, i.path, i.is_dir())

# print(os.walk('/root'))
#

# lst = os.listdir()
# print(lst)
#从文件中查找结尾为py的文件
# for i in lst:
#     if i.endswith('py'):
#         print(i)
# for i in lst:
#     if i.startswith('123') and i.endswith('.txt'):
#         print(i)

import glob
# print(glob.glob(('*.py'))) #以.py结束的文件
# print(glob.glob('y*.py'))
# print(glob.glob('**/*.py', recursive=True)) #标示单是任意层文件夹

import fnmatch
print(fnmatch.fnmatch('ytwwww.py', 'yt?.py'))
