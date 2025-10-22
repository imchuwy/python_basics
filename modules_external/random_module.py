import random

for i in range(3):
    print(random.randint(10, 20))


members = ['Oscar','Mosh','Phil','Dan']
leader = random.choice(members)
print(leader)