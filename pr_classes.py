'''
Define a new type called Person. This class should have:
- name
- talk method
'''

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'Hi, I am {self.name}')


oscar = Person('Oscar Chu')
oscar.talk()

bob = Person('Bob Smith')
bob.talk()