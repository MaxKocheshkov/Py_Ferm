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
    
### Task 2
goose_1 = Goose('гусь Серый', 2)
goose_1.goose_voice()
goose_1.Bird_feeding()
goose_1.Bird_receipt()
print('######')
goose_2 = Goose('гусь Белый', 1.6)
goose_2.goose_voice()
goose_2.Bird_feeding()
goose_2.Bird_receipt()
print('######')
chicken_1 = Chicken('курица Ко-Ко', 3.4)
chicken_1.chiken_voice()
chicken_1.Bird_feeding()
chicken_1.Bird_receipt()
print('######')
chicken_2 = Chicken('курица Кукареку', 2.5)
chicken_2.chiken_voice()
chicken_2.Bird_feeding()
chicken_2.Bird_receipt()
print('######')
duck_1 = Duck('утка Кряква', 1.2)
duck_1.duck_voice()
duck_1.Bird_feeding()
duck_1.Bird_receipt()
print('######')
cow_1 = Cow('корова Манька', 500)
cow_1.cow_voice()
cow_1.Ungulates_feeding()
cow_1.cow_receipt()
print('######')
sheep_1 = Sheep('овца Барашек', 100)
sheep_1.sheep_voice()
sheep_1.Ungulates_feeding()
sheep_1.sheep_receipt()
print('######')
sheep_2 = Sheep('овца Кудрявый', 150)
sheep_2.sheep_voice()
sheep_2.Ungulates_feeding()
sheep_2.sheep_receipt()
print('######')
goat_1 = Goat('коза Рога', 125)
goat_1.goat_voice()
goat_1.Ungulates_feeding()
goat_1.goat_receipt()
print('######')
goat_2 = Goat('коза Копыта', 140)
goat_2.goat_voice()
goat_2.Ungulates_feeding()
goat_2.goat_receipt()
print('######')
