from Classes1 import WarcraftSpecs
from Classes2 import Healer


class Priest(Healer):
    def __init__(self, hp, damage, mana, insanity=0):
        super().__init__(hp, damage, mana)
        self.insanity = insanity

    def is_dps(self):
        if self.insanity > 0:
            print('It\'s a Shadow Priest!')
            return True
        else:
            print('This Priest is a Healer.')
            return False

    def bloodlust(self):
        if self.is_dps():
            return self.damage * 1.3
        else:
            return self.mana * 1.3


shadow = Priest(100, 250, 60, 80)
shadow.is_dps()
shadow.bloodlust()
