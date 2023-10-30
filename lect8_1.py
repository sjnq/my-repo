"""#cls
class MyClass:
    count = 0

    def __init__(self, num):
        self.count = num

    @classmethod
    def clsMethod(cls):
        cls.count += 1 
        print(f"cls count = {cls.count}")

    def instMethod(self):
        self.count += 1 
        print(f"instance = {self.count}")

MyClass.clsMethod()

obj = MyClass(10)

obj.instMethod()
print(obj.count)

print(MyClass.count)
print(MyClass.count)
"""
#
class Champion :
    lv = 1
    movSpd = 0
    basicMovSpd = 325
    atkSpd = 0.658
    
    def __init__(self, champion, speed):
        self.hp = 100
        self.champion = champion
        self.level = 1
        self.setSpead(speed)
        self.setAtkSpd()
        self.setMovSpd()
        
    def setAtkSpd(self):
        self.atkSpd = 0.658*((1.0334)**(Champion.lv - 1) )
    
    def beAtk(self,dem):
        print("be attack", dem, 1-10.0/(100.0+100))
        self.dem = dem*(100.0/(100.0+100))
        print(self,dem)
        self.hp = self.hp-self.dem
        
    def setSpead(self, sp):
        if (sp == 1):
            self.spead = 50
        else:
                self.spead = 0
    
    def setPovSpd(self):
        print("set Mov Spd")
        self.movSpd = (20 + self.spead)*(1.00)*(100)
        
    def printStatus(self):
        print("champNam:%s, hp:%f, lv%d, atkSpd:%f" %(self.champion,))

        
ashe = Champion("ashe", 474.0)
aipo = Champion("aipo", 520.0)

#"""
class champion :
    def __init__(self, name):
        self.name = name
        self.level = 1
        
class Yasuo(Champion):
    def getName(self) :
        print(self.name)
        
    def attck(self,key):
        print(f"attack = (key)")
        
    def levelup(self):
        self.level += 1
        
    def getlevel(self):
        print(self.level)
        
        
class Garen(Champion):
    def getName(self) :
        print(self.name)
        
    def attck(self,key):
        print(f"attack = (key)")
        
    def levelup(self):
        self,level += 1
        
    def getlevel(self):
        print(self.level)
        
        
user1 = Yasuo("python")
user2 = Garen("hello")

user1.getName
user1.getlevel

user2.getName()
user2.getlevel()

#
class Champion :
    def __init__(self, name) :
        self.name = name
        self.level = 1
        
    def getName(self):
        print(self.name)
        
    def attck(self, key):
        print(f"attack = {key}")
        
    def levelup(self):
        self.level += 1
    
    def getLevel(self):
        print(self.level)
class Yasuo(Champion): ()

class Garen(Champion): ()     

user1 = Yasuo("python")
user2 = Garen("hello")

user1.getName()
user1.getLevel()

user2.getName()
user2.getLevel()

#########
class Champion :
    def __init__(self, name) :
        self.name = name
        self.level = 1
    
    def attck(self, key) :
        print(f"attack = {key}")
    
    def levelup(self) :
        self.level += 1
    
    def getLevel(self) :
        print(self.level)


class Yasuo(Champion) :
    def attck(self, key):
        print(f"attack - {key} steel tempest")
        return


class Garen(Champion) :
    def attck(self, key):
        print(f"attack - {key} demacian justice")
        return
    
user1 = Yasuo("python")
user2 = Garen("hello")

user1.getLevel()
user2.getLevel()

user1.attck("q")
user2.attck("r")

user1.levelup()
user2.levelup()

user1.getLevel()
user2.getLevel()
    
#데코레이터 @abstractmethod 사용
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circ = Circle(5)
rect = Rectangle(4, 6)

print(circ.area())
print(rect.area())

sett = [circ, rect]
for st in sett :
    print(st.area())

######
class Person:
    def __init__(self, name, age, num):
        self._name = name
        self._age = age
        self._number = num

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def number(self):
        return self._number

    @name.setter
    def name(self, new):
        self._number = new

    @age.setter
    def age(self, nAge):
        self._age = nAge
        
user1 = Person("Alic3"), 30, "01011112222"


print(user1.age)
print(user1._age)
print(user1.name)
print(user1._name)
print(user1.number)
print(user1._number)

user1._age = 21
user1.age = 23
print(user1.age)


#####
class Person :
    def __init__(self, name, age, num) :
        self.name = name
        self.age = age
        self.number = num
    
    def getName(self) :
        return self.name
    
    def getAge(self) :
        return self.age
    
    def getNumber(self) :
        return self.number

class Student(Person) : ()

class Teacher(Person) : ()

def getPersonName(person) :
    return person.getName()

user1 = Student("alice", 23, "01011112222")
user2 = Teacher("bob", 25, "01033334444")

print(getPersonName(user1))
print(getPersonName(user2)) 
#
def __init__(self, name, age, num) :
		self.name = name
		self.age = age
		self.number = num

def getName(self) :
        return self.name

def setName(self, newname) :
        return self.name = newName

def getNumber(self) :
        return self.number

def setNumber(self, newNum) :
        self.number = newNum
        return

p1= Person("python", 23, "01012345678")
p1.getNumber()

p1.setNumber("11111111111")
p1.setNumber("22222222222") """