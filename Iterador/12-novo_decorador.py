from decorator import my_decorator, upper_case_decorator, split_string

@my_decorator
def my_function():
    print("Dentro da função")

my_function()

@upper_case_decorator
def text():
    return "Olá mundo"
print(text())

@split_string
def example():
    return "Aprendendo python e criando decorators"

print(example())