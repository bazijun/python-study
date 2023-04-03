try:
    print(5/0)
except ZeroDivisionError: # 异常出现
    print("You can't divide by zero!")
else: # 没有异常走的代码
	print("no exception")
