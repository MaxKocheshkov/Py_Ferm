### Task 1
class Ferm_animals:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        print(f'{self.name} весит {self.weight} кг')
    def Voice(self):
      pass


###
class Bird(Ferm_animals):
    def Bird_feeding(self):
      print(self.name + " есть зерно")

    def Bird_receipt(self):
      print(self.name + " дает яйца")
###
class Ungulates(Ferm_animals):
    def Ungulates_feeding(self):
      print(self.name + " есть траву")
###
class Goose(Bird):
  def goose_voice(self):
    print(f'{self.name} говорит "Га-га-га"')
###
class Chicken(Bird):
  def chiken_voice(self):
    print(f'{self.name} говорит "Ко-ко-ко"')
###
class Duck(Bird):
  def duck_voice(self):
    print(f'{self.name} говорит "Кря-кря"')
###
class Cow(Ungulates):
  def cow_receipt(self):
    print(self.name + " дает молоко")

  def cow_voice(self):
    print(f'{self.name} говорит "Мууууу"')
###
class Sheep(Ungulates):
  def sheep_receipt(self):
    print(self.name + " дает шерсть")

  def sheep_voice(self):
    print(f'{self.name} говорит "Бееее"')
###
class Goat(Ungulates):
  def goat_receipt(self):
    print(self.name + " дает шерсть")

  def goat_voice(self):
    print(f'{self.name} говорит "Мееее"')
