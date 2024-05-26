"""
Abstract Factory

    Car => Benz, BMW => Coupe, Suv
        benz suv => gla, glc
        bmw suv => x1, x2

        benz coupe => cls, E-class
        bmw coupe => m2, m4
"""

from abc import ABC, abstractmethod

#-------------------<Abstract Classes>-------------------

class Car(ABC):
    @abstractmethod
    def call_suv(self):
        pass

    @abstractmethod
    def call_coupe(self):
        pass


class Coupe(ABC):
    @abstractmethod
    def creating_coupe(self):
        pass

class Suv(ABC):
    @abstractmethod
    def creating_suv(self):
        pass

#------------------------------------------------------

class Benz(Car):
    @staticmethod
    def call_coupe(model):
        return model()
    
    @staticmethod
    def call_suv(model):
        return model()
    
#------------------------------------------------------

class Bmw(Car):
    @staticmethod
    def call_coupe(model):
        return model()
    
    @staticmethod
    def call_suv(model):
        return model()

#------------------------------------------------------
    
class Gla(Suv):
    def creating_suv(self):
        return "Creating Suv Benz Car - Gla Model..."
    
#------------------------------------------------------
    
class Glc(Suv):
    def creating_suv(self):
        return "Creating Suv Benz Car - Glc Model..."
    
#------------------------------------------------------
    
class X1(Suv):
    def creating_suv(self):
        return "Creating Suv BMW Car - X1 Model..."
    
#------------------------------------------------------
    
class X2(Suv):
    def creating_suv(self):
        return "Creating Suv BMW Car - X2 Model..."
    
#------------------------------------------------------
    
class Cls(Coupe):
    def creating_coupe(self):
        return "Creating Coupe Benz Car - Cls Model..."
    
#------------------------------------------------------
    
class E_class(Coupe):
    def creating_coupe(self):
        return "Creating Coupe Benz Car - E-class Model..."
    
#------------------------------------------------------
    
class M2(Coupe):
    def creating_coupe(self):
        return "Creating Coupe BMW Car - M2 Model..."
    
#------------------------------------------------------
    
class M4(Coupe):
    def creating_coupe(self):
        return "Creating Coupe BMW Car - M4 Model..."
    
#-------------------<Client>--------------------------

def create_coupe(car, model):
    coupe = car.call_coupe(model)
    result = coupe.creating_coupe()
    return result

def creating_suv(car, model):
    suv = car.call_suv(model)
    result = suv.creating_suv()
    return result

#-------------------<Test>----------------------------

benz = Benz()
bmw = Bmw()

print(create_coupe(benz, Cls))
print("=" * 100)
print(create_coupe(benz, E_class))
print("=" * 100)
print(create_coupe(bmw, M2))
print("=" * 100)
print(create_coupe(bmw, M4))
print("=" * 100)
print(creating_suv(benz, Gla))
print("=" * 100)
print(creating_suv(benz, Glc))
print("=" * 100)
print(creating_suv(bmw, X1))
print("=" * 100)
print(creating_suv(bmw, X2))
