class Warrior:
    warrior_list = []
    def __init__(self, name, strength, stamina):
        self.name = name
        self.level = 10
        self.strength = strength
        self.health = 100
        self.gold = 25
        self.stamina = stamina
        Warrior.warrior_list.append(self)
    def attack(self, oponent, *args, **kwargs):
        damage = self.level * 0.2
        full_damage = self.strength+damage
        oponent.health -= full_damage
        self.stamina -= damage
        print(f"{self.name} attacked {oponent.name} for {full_damage} damage, {oponent.name}'s Health is now {oponent.health}")
        return self
    def super_attack(self, oponent):
        damage = self.level * 0.8
        full_damage = self.strength+damage
        oponent.health -= full_damage
        self.stamina -= damage
        print(f"{self.name} attacked {oponent.name} for {full_damage} damage, {oponent.name}'s Health is now {oponent.health}")
        return self
    def meditate(self):
        if self.gold - 10 >= 0:
            self.gold -= 10
            if self.health + 15 < 100:
                self.health += 15
            if self.stamina + 15 < 100:
                self.stamina += 15
            else: 
                self.health = 100
                self.stamina = 100
        else:
            print('Not enough gold to heal get gold by doing work or battles')
        print(f"Heal the soul with meditation Health: {self.health} Stamina: {self.stamina} Cost 10 gold")
        return self 
    def level_up(self):
        bonus_levels = [16,22,26,32,36]
        level = self.level + 2
        if level in bonus_levels:
            self.health += 10
            self.level += 2
            print(f"Yay! You Reached A bonus level health also increased by 10 \n level: {self.level} health: {self.health}")
        else:
            self.level += 2
            print(f"{self.name} New level: {self.level}")
        return self
    def level_strength(self):
        self.strength += 5
        print(f"{self.name} New strength: {self.strength}")
        return self
    def display_info(self):
        return f"Warrior info, \n Name: {self.name} \n Level: {self.level} \n Strength: {self.strength} \n Health: {self.health} \n Stamina: {self.stamina} \n Gold: {self.gold}"


class Ninja(Warrior):
    def __init__(self, name, strength, stamina):
        super().__init__(name, strength, stamina)
        self.level = 8
        self.ninjistu = 12
        self.health= 80
        self.gold = 20
    def meditate(self):
        self.ninjistu += 1
        self.gold -= 5
        print(f"Heal the soul with meditation Health: {self.health} Stamina: {self.stamina} Ninjistu: {self.ninjistu} Cost 15 gold")
        super().meditate()
        return self
    def attack_ninja(self, oponent, damage, *args, **kwargs):
        
        return super().attack(oponent,damage, *args, **kwargs)

ninja1 = Ninja("ninjaBob", 40, 160)
ninja1.meditate()
print(ninja1.display_info())
w1 = Warrior('CadenTheNurmal', 20, 50)
w2 = Warrior('Destroyer', 40, 80)
ninja1.attack_ninja(w1, 20)
# to_be_attacked = input("Who do you want to attack? ")
# print(to_be_attacked)
# w1.attack(w2)
# ninja1.attack(w1)
# w1.super_attack(w2).level_up().level_strength()
# print(w1.meditate().level_strength().level_up().display_info())
# print(w2.display_info())
# w2.meditate()
# w1.level_up()
# print(w2.display_info())
# w1.level_up()