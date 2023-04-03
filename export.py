# python中所有变量和函数不用做`导出`操作，其都在模块的命名空间中

# 导入整个模块
import first
from function import * # 不推荐的做法

# 从 一个模块导出 某一个或多个变量、方法、类
from function import info 
from cla import Cat, Animal

# as 重命名导出的变量或方法以及模块
import function as MyPrimary
from function import infoTo as bzjTo 




