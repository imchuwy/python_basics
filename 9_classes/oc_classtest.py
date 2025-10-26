'''
Self practice
'''
class Player:
    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname
        self.stats = {
            "Shooting": 80,
            "Defence": 80,
            "Dribbling": 80
        }
    def shoot(self):
        print(f'{self.firstname} {self.surname} shoots')
    def tackle(self):
        print(f'{self.firstname} {self.surname} tackles')
    def dribble(self):
        print(f'{self.firstname} {self.surname} dribbles')
    def show_stats(self):
        for stat, value in self.stats.items():
            print(f"{stat.capitalize()}: {value}")

##Adding
#Messi = Player('Leonel','Messi')
#Messi.height = 170
#print(Messi.height)
#Messi.shoot()
#Messi.show_stats()

class Defender(Player): #INHERITANCE!
    def __init__(self, firstname, surname):     #Initialse self
        super().__init__(firstname, surname)    # Super() access methods from parent superclass inside child. Here we initalise the parent
        self.stats["Defence"] += 10             # Add +10 for defenders
    def position(self):
        print('Defender')


Terry = Defender('John','Terry')
Terry.position()
Terry.show_stats()
