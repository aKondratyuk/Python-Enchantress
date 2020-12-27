def charge(self):
    return "100%"


class MetaChargableCar(type):
    def __init__(cls, clsname, superclasses, attributedict):
        if clsname == "Tesla":
            cls.charge = charge


class Car:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color


class Ferrari(Car, metaclass=MetaChargableCar):
    def __init__(self, speed, color):
        super().__init__(speed, color)
        self.engine_type = "benzine"


class Tesla(Car, metaclass=MetaChargableCar):
    def __init__(self, speed, color):
        super().__init__(speed, color)
        self.engine_type = "electric"


if __name__ == '__main__':
    ferrari_espando = Ferrari("300 km/h", "red")
    tesla_p100 = Tesla("220 km/h", "gray")
    print("Tesla charged to", tesla_p100.charge())

