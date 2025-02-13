from test import my_decorator, uppercase_decorator, split_string

@my_decorator
def my_function():
    print("Dentro da função")
    
my_function()

@split_string
@uppercase_decorator
def text():
    return "Hello WOrld"

print(text())

@split_string
@uppercase_decorator
def example():
    return "Aprendendo Python e criando decorators"

print(example())