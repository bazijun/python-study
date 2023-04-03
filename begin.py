# https://juejin.cn/post/6844903765410070535#heading-1
# 鉴定为和JS差不多, 关键词依旧很通用，但是相对JS相对都是简写
print('hello pyhton!')

hello = 'hello pyhton!'

# 以下方法只输出新的字符串，不改变原字符串
# 每个单词的首字母都改为大写
hello.title()
# 全大写
hello.upper()
# 全小写
hello.lower()

# rstrip() 删除右侧空白，lstrip() 删除左侧空白，strip() 删除两端空白。
frist = 'b'
end = 'zj'
bzj = frist + end

# 在Python 2中，print语句的语法稍有不同: 但已经可以使用函数式print
# print "Hello Python 2.7 world!" 


# 和js(几乎所有语言)同样的浮点数 问题
a = 0.2 + 0.1 # 0.30000000000000004 
b = 3 * 0.1  # 0.30000000000000004


# 非js那样的隐式转换，数字拼接字符串会报类型错误，使用 `str()` 转换数字即可
age = 12
print(str(age) + '12') 

# 列表 以下操作都会改变原列表
list = []
# append 列表最后添加一个元素
list.append('b') 
list.append('k')
# insert 插入
list.insert(2, 'j')
# 直接通过索引修改列表元素
list[1] = 'z'
# 获取最后一个元素可以用 -1，如 list[-1] 是获取最后一个元素，list[-2] 是获取倒数第二个元素。
print(list, list[-1])

del list[1] #删除某项
print(list)

list_2 = ['zhangsan', 'lisi', 'bob', 'alex']
list_2.sort() # ['alex', 'bob', 'lisi', 'zhangsan']
# 反转
list_2.sort(reverse=True) # ['zhangsan', 'lisi', 'bob', 'alex']

# 以下操作不会改变原列表
sorted(list_2, reverse=True)


# 循环
for item in list_2:
    print(item)

# 对列表进行简单的计算
list_3 = [1,2,3,4,6]
print('min', min(list_3)) #计算最小值
print('max', max(list_3)) #计算最大值
print('sum', sum(list_3)) #计算总和

# 计算平方
square = 2**3 # 2的3次方

# 列表解析
square_list = [value**2 for value in range(1,11)] # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 列表切片（类似 sub）
names = ['aa','bb','cc','dd','dd']
print('1:4',names[1:4]) # ['bb', 'cc', 'dd']
print(':4',names[:4]) # 默认从列表开头开始到4
print('1:',names[1:]) # 从1自动取到列表末尾
print('-3:',names[-3:]) # 返回最后三个元素

# 复制列表 (拷贝: 既不受原列表影响)
names2 = names[:] # ['aa','bb','cc','dd']
# 直接赋值 names改变 names2也会改变, 参考深拷贝

print('set', set(names)) # set 去重

# 元组： 不可变的列表, 用括号定义
food = ('apple', 12)

# 条件判断 本质 是 True 与 False 的表达式
# 检查是否相等，用 ==
# 检查是否不相等，用 !=
# 数字比较 >、 <、 >=、 <=
# 多个条件与 and
# 多个条件或 or
# 判断列表是否包含某元素 in
print('apple' in food) # 包含某元素
print('Bzj' not in food) # 不包含某元素

# if
if 'apple' == food:
    print('不可能')
elif 'apple1' in food:
    print('有可能')
else:
    print('肯定')


# 字典 用{} 包裹
user = {'name': '张三', 'age': 12}
user['name'] # 字典访问 -> 张三
user['city']='beijing' # 添加键值对
user['city'] = 'chendu' # 修改键值对
del user['age'] # 删除键值对
print('user', user)

# 通过 for k,v in obj.items() 的方式遍历所有的键值对，k 代表键，v 代表值。
# 如果不需要用值，可以用 obj.keys() 遍历出所有的键。
# 遍历所有值 obj.values()

# 用户输入
msg = input('请输入') # Python 2.7 请使用 raw_input()
print(msg, '√')


