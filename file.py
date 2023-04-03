# with 关键字能让文件在合适的时候自动关闭
# open 可以打开文件
# read 直接阅览整个文件
# rstrip 清除最后一行 由于read方法所产生的空行

with open('cla.py', encoding='utf-8') as cla_py:
    contents = cla_py.read()
    print(contents.rstrip())

# 逐行读取
with open('cla.py', encoding='utf-8') as file_obj:
    for line in file_obj:
        print(line.rstrip())

# 写入文件
# open 的第二个参数 参考如下
    # r ：只读 （默认）。
    # w : 只写。如果文件不存在则创建，如果文件存在则先清空，再写入。
    # a ：附加模式，写入的内容追加到原始文件后面。如果文件不存在则创建。
    # r+ ：可读可写。

with open('test.txt', 'w') as file_obj:
    file_obj.write("I love python")


import json

userInfo = {'username': '浩二', 'age': 24}

with open('json.txt', 'w') as obj:
    json.dump(userInfo, obj) # dump() 写入

with open('json.txt') as obj:
    content = json.load(obj) # load() 文件
    print(content)

