
# Soldier


class Soldier:
    def __init__(self, health, strength):
        health.self = health
        strength.self = strength
    def attack(self):
        return strength.self

    def receiveDamage(self, damage):
        damage.self = damage
        health.self -= damage.self

# Viking


class Viking(Soldier):
    def __init__(self,name , health, strength):
        self.name = name
        super()__init__(health, strength)
    def attack(self):
        return Soldier.attack(self)
    def receiveDamage(self, damage):
        damage.self = damage
        health.self -= damage.self
        if health.self <= 0:
            return f"{name.self} has died in act of combat"
        if health.self > 0:
            return f"{name.self} has received {damage.self} points of damage"
    def battleCry(self):
        return "Odin Ows You All!"


# Saxon


class Saxon:
    pass

# War


class War:
    pass
