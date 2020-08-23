
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
    def attack(self):
        return Soldier.attack(self)
    def receiveDamage(self, damage):
        Soldier.receiveDamage(self, damage)
        if self.health <= 0:
            return f"{self.name} has died in act of combat"
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
    def battleCry(self):
        return "Odin Owns You All!"


# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    def attack(self):
        return Soldier.attack(self)
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return f"A Saxon has died in combat"
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
# War


class War:

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    def vikingAttack(self):
        import random
        sax = random.choice(self.saxonArmy)
        vik = random.choice(self.vikingArmy)
        damage = vik.attack()
        sax.receiveDamage(damage)
        if sax.health <= 0:
            self.saxonArmy.remove(sax)
        else:
            return sax.receiveDamage(damage)

    def saxonAttack(self):
        import random
        sax = random.choice(self.saxonArmy)
        vik = random.choice(self.vikingArmy)
        damage = sax.attack()
        vik.receiveDamage(damage)
        if vik.health <= 0:
            self.vikingArmy.remove(vik)
        else:
            return vik.receiveDamage(damage)


    def showStatus(self):
            v_size = len(self.vikingArmy)
            s_size = len(self.saxonArmy)
            if v_size == 0:
                return f"Saxons have fought for their lives and survive another day..."
            if s_size == 0:
                return f"Vikings have won the war of the century!"
            if v_size != 0 and s_size != 0:
                return f"Vikings and Saxons are still in the thick of battle."