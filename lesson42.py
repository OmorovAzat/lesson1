# Декораторы
# def hello():
#     return 'Hello, I am func "hello"'
#
#
# def super_func(func):
#     print('Hello, I am func "super_func"')
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello
# print(test())

def make_title(fn):
    def wrapped():
        title = fn()
        title = title.capitalize()
        title = title.replace(',', '')
        return title
    return wrapped


@make_title
def hi():
    return 'hello, world'


print(hi())

