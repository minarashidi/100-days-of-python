# Unlimited Arguments/Unlimited Positional Arguments: *args
def add(*args):
    print(type(args))
    print(args[1])
    # return sum(args)
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 2, 3))


def calculate(n, **kwargs):
    print(type(kwargs))
    print(kwargs["add"])
    print(kwargs.get("subtract"))
    print(kwargs)
    n += kwargs.get("add")
    n *= kwargs.get("multiply")
    print(n)


calculate(2, add=2, multiply=3)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.year = kwargs.get("year")
        self.color = kwargs.get("color")
        self.mileage = kwargs.get("mileage")
        self.speed = kwargs.get("speed")
        self.acceleration = kwargs.get("acceleration")
        print(kwargs)
        print(self)


new_car = Car(make="Ford")
print(new_car)
