import requests


def first_func():
    pass


class Human:
    pass

rq = requests
first_f = first_func
nick = Human

print(rq.__name__)
print(first_f.__name__)
print(nick.__name__)

#можно узнать тип обьекта
print(type(rq))
print(type(first_f))
print(type(nick))

#можно узнать список обьектов и атрибутов
name = ""
for method in dir(name):
    print(method)

print("hasattr - ")
print(hasattr(name, "reverse"))
print(hasattr(name, "index"))

print("getattr - ")
print(getattr(name, "startswith"))

#callable() отвечает на вопрос можно ли вызвать обьект

print(callable(name))
print(callable(first_func))

class A:
    pass

class B(A):
    pass


# МОЖЕТ ПОНЯТЬб НАСЛЕДУЕТСЯ ЛИ ЄТОТ КЛАС ОТ ДРУГОГО
print(issubclass(A, B))
print(issubclass(B, A))

obj1 = B()
print(isinstance(obj1, A))


import inspect

print(inspect.ismodule(requests))
print(inspect.ismodule(obj1))
print(inspect.isclass(requests))

print(inspect.getmodule(requests.get))


import  sys
#можете узнать расположение интерпритатора вашего проекта
print(sys.executable)
print(sys.version)

print(sys.platform)






