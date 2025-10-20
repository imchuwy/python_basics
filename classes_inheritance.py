'''
We don't want to repeat code. 
DRY - Don't, Repeat, Yourself
'''
class Tree:
    def grow(self):
        print('growing slowly')


class Plant:
    def grow(self):
        print('growing slowly')



##Instead
class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    pass #This makes python happy. No empty class


class Cat(Dog):
    def speak(self):
        print('meow')


dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.speak()