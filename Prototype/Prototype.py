from copy import deepcopy

class Person:
    def __init__(self, name, age) :
        self.name = name
        self.age = age

class Prototype:
    def __init__(self) :
        self._object = {}

    def register(self, name, obj):
        self._object[name] = obj

    def unregister(self, name):
        del self._object[name]

    def clone(self, name, **kwargs):
        cloneObj = deepcopy(self._object.get(name))
        cloneObj.__dict__.update(kwargs)
        return cloneObj
    

P1 = Person('Ali', 24)

Pro1 = Prototype()
Pro1.register('person1', P1)
personcopy = Pro1.clone('person1')

print(personcopy.__dict__)

personcopy2 = Pro1.clone('person1', age= 56)

print(personcopy2.__dict__)