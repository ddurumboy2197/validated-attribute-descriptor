class ValidatedAttribute:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{self.name} attribute must be a positive integer")
        instance.__dict__[self.name] = value


class MyClass:
    x = ValidatedAttribute()

    def __init__(self, x):
        self.x = x


# Test
obj = MyClass(10)
print(obj.x)  # 10

try:
    obj.x = -5
except ValueError as e:
    print(e)  # x attribute must be a positive integer

try:
    obj.x = 3.14
except ValueError as e:
    print(e)  # x attribute must be a positive integer

try:
    obj.x = "hello"
except ValueError as e:
    print(e)  # x attribute must be a positive integer
