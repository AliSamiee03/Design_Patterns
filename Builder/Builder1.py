'''
    Builder
'''
from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod
    def get_wheel(self):
        pass

    @abstractmethod
    def get_body(self):
        pass

    @abstractmethod
    def get_engine(self):
        pass

#------------------------------------------------------
class Wheel():
    size = None

class Body():
    shape = None

class Engine():
    hp = None


#-----------------------------------------------------

class Benz(Builder):
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 25
        return wheel

    def get_body(self):
        body = Body()
        body.shape = 'SUV'
        return body

    def get_engine(self):
        engine = Engine()
        engine.hp = 400
        return engine


class Bmw(Builder):
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 20
        return wheel

    def get_body(self):
        body = Body()
        body.shape = 'Sedan'
        return body

    def get_engine(self):
        engine = Engine()
        engine.hp = 450
        return engine

#------------------------------------------------------------

class Car:
    def __init__(self):
        self.__wheel = None
        self.__body = None
        self.__engine = None

    def set_wheel(self, wheel):
        self.__wheel = wheel

    def set_body(self, body):
        self.__body = body

    def set_engine(self, engine):
        self.__engine = engine

    def show_details(self):
        print(f'Body : {self.__body.shape}')
        print(f'Wheel : {self.__wheel.size}')
        print(f'Engine : {self.__engine.hp}')

#--------------------------------------------------------------------

class Director:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_car(self):
        car = Car()
        body = self.__builder.get_body()
        wheel = self.__builder.get_wheel()
        engine = self.__builder.get_engine()
        car.set_body(body)
        car.set_wheel(wheel)
        car.set_engine(engine)
        return car

bmw = Bmw()

director = Director()
director.set_builder(bmw)
car1 = director.get_car()
car1.show_details()