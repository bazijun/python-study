# 函数

def great():
    print('做得好！')

great()

def info(name='小把', age = 18) -> str:
    return name + '-' + str(age)

print(info('田中<本物>',34)) # 位置实参, 按入参顺序传递
print(info(age=99)) # 关键字实参，直接指定入参

# 传递任意数量的实参
def person(*age):
    print(age)

person('name',12,'b')

# 使用任意数量的关键字实参
def infoTo(a,**info):
    profile = {}
    profile['first_name'] = a
    profile.update(info)
    return profile

print(infoTo('steven', city='beijing', age=18))

