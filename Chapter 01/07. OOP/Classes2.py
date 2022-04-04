from Classes1 import WarcraftSpecs


class Healer(WarcraftSpecs):
    def __init__(self, hp, damage, mana):
        super().__init__(hp, damage)
        self.mana = mana

    def bloodlust(self):
        return self.mana * 1.33


holy = Healer(100, 50, 210)
print(holy.bloodlust())

warlock = WarcraftSpecs(200, 50)
print(warlock.bloodlust())