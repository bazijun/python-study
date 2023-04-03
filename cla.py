class MiniCat():
    # __init__ 即是构造方法； self 即是 this
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color
    
    def eat(self):
        print('cat ' + self.name + ' color ' + self.color + ', now eat')

    def run(self):
        print('cat ' + self.name + ' color ' + self.color + ', now run')
    
    def updata_color(self, color: str) -> None:
        self.color = color


my_cat = MiniCat('juju', 'orange')
my_cat.updata_color('red')
my_cat.eat()

# 继承
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('Animal ' + self.name + ' run')


# 父类往子类括号一装就是继承，然后在构造函数头用super调用父类构造方法就ok了
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    # 扩展方法
    def play(self):
        print('Cat ' + self.name + ' play')

    # 方法重载
    def run(self):
        print('Cat ' + self.name + ' run')


cat = Cat('Tony', 2)
cat.run()
