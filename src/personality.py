from random import randint

def gen_atrib():
    a = []
    for j in range(1, 5):
        a.append(randint(1, (100 - sum(a)) - (5 - j)))
    a.append(100 - sum(a))
    return a

def __init__(self):
    self.neuroticism, self.openness, self.conscientiousness, self.extraversion, self.agreeableness = gen_atrib()

def personality_traits(self):
    return [self.neuroticism, self.openness, self.conscientiousness, self.extraversion, self.agreeableness]

def shoot(self):
    print("Shooting")

def search(self):
    print("Searching")

def talk(self):
    print("Talking")

def turrets_generator():
    return type("Turrets", (), {"__init__" : __init__, "personality_traits" : personality_traits, "shoot" : shoot, "search" : search, "talk" : talk})()

def main():
    a = turrets_generator()
    b = a.personality_traits()
    print(b, sum(b))
    a.shoot()
    a.search()
    a.talk()

if __name__ == "__main__":
    main()