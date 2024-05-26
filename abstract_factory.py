from abc import ABC, abstractmethod

#-------------------------------------
class Car(ABC):
    @abstractmethod
    def call_suv(self):
        pass

    @abstractmethod
    def call_coupe(self):
        pass

#-------------------------------------

class Benz(Car):
    def call_suv(self):
        return Gla()

    def call_coupe(self):
        return Cls()
    
#-------------------------------------

class Bmw(Car):
    def call_suv(self):
        return X1()
    
    def call_coupe(self):
        return M2()

#-------------------------------------
    
class Coupe(ABC):
    @abstractmethod
    def creating_coupe(self):
        pass

#-------------------------------------

class Suv(ABC):
    @abstractmethod
    def creating_suv(self):
        pass

#-------------------------------------

class Gla(Suv):
    def creating_suv(self):
        print("Creating Gla => Suv car...")

#-------------------------------------

class Cls(Coupe):
    def creating_coupe(self):
        print("Creating Cls => Coupe car...") 

#-------------------------------------

class X1(Suv):
    def creating_suv(self):
        print("Creating X1 => Suv car...")

#-------------------------------------

class M2(Coupe):
    def creating_coupe(self):
        print("Creating M2 => Coupe car...") 

#-------------------------------------

def client_suv(order):
    suv = order.call_suv()
    suv.creating_suv()

#-------------------------------------

def client_coupe(order):
    coupe = order.call_coupe()
    coupe.creating_coupe()

#-------------------------------------

benz = Benz()
bmw = Bmw()

client_coupe(benz)
print('=' * 50)
client_suv(benz)
print('=' * 50)
client_suv(bmw)
print('=' * 50)
client_coupe(bmw)