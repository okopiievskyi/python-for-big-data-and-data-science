def my_fun(my_fun2):
    def my_fun3(*arg, **kwarg):
        print("hello!")
        return my_fun2(*arg, **kwarg)
    return my_fun3
@my_fun
def my_add(arg1, arg2):
    return arg1+arg2
print(my_add(3,4))