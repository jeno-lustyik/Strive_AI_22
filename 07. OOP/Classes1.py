class WarcraftSpecs:
    def __init__(self, damage, hp):
        self.damage = damage
        self.hp = hp
        pass

    def bloodlust(self):
        return self.damage * 1.3