sum_weight = []  # общий вес популяции
max_weight_name = {}


class Animal:
    status = 'hungry'  # когда будем кормить, будет меняться статус
    name = 'name defined by user'
    weight = 0  # кг
    voice = None

    def feed(self):
        self.status = 'fed'

    # def voice_recognition(self):
    #   if self.voice == 'му':
    #     print("That's a cow!")

    def __init__(self, n, w):
        self.name = n
        self.weight = w
        sum_weight.append(self.weight)
        max_weight_name[self.name] = self.weight


class Bird(Animal):
    eggs = 'there are some eggs to collect'

    def collect_eggs(self):
        self.eggs = 'all eggs are collected'


class Artiodactyles_to_milk(Animal):
    milk_status = 'it has some milk today'

    def milk(self):
        self.milk_status = 'the animal seems to be happy after milking'


class Goose(Bird):
    voice = 'га-га-га'


goose_1 = Goose('Серый', 8)
goose_2 = Goose('Белый', 12)
goose_2.collect_eggs()  # здесь и далее - будем выполнять с животными методы, чтобы убедиться, что всё работает - выводить через print

print(goose_1.name, goose_1.weight, goose_1.eggs)
print(goose_2.name, goose_2.weight, goose_2.eggs)


class Cow(Artiodactyles_to_milk, Animal):
    voice = 'му-у-у'


cow_1 = Cow('Манька', 500)
print(cow_1.name, cow_1.weight, cow_1.milk_status)


class Sheep(Animal):
    voice = 'бе-е-е'
    wool_status = 'it has lots of wool'

    def cut_the_wool(self):
        self.wool_status = 'it looks almoust naked now'


sheep_1 = Sheep('Барашек', 125)
sheep_1.cut_the_wool()

sheep_2 = Sheep('Кудрявый', 97)

print(sheep_1.name, sheep_1.weight, sheep_1.wool_status)
print(sheep_2.name, sheep_2.weight, sheep_2.wool_status)


class Chicken(Bird, Animal):
    voice = 'курлык'


chicken_1 = Chicken('Ко-Ко', 4)
chicken_2 = Chicken('Кукареку', 3)

print(chicken_1.name, chicken_1.weight, chicken_1.eggs)
print(chicken_2.name, chicken_2.weight, chicken_2.eggs)


class Goat(Artiodactyles_to_milk, Animal):
    voice = 'ме-е-е'


goat_1 = Goat('Рога', 50)
goat_2 = Goat('Копыта', 35)
goat_2.milk()

print(goat_1.name, goat_1.weight, goat_1.milk_status)
print(goat_2.name, goat_2.weight, goat_2.milk_status)


class Duck(Bird, Animal):
    voice = 'кря-кря'


duck_1 = Duck('Кряква', 2)
print(duck_1.name, duck_1.weight, duck_1.eggs)

print('\nСуммарный вес животных: ', sum(sum_weight))

final_dict = dict([max(max_weight_name.items(),
                       key=lambda key_value: key_value[1])])  # нашел в интернете, как работает - понимаю слабо
print('\nСамое тяжелое животное: ', final_dict)
# print(input(str('Какой звук вы услышали, ', Goat.voice)))
print(
    '\nЕсли вы хотите определить животное по звуку, выберите звук, который вы слышите: \n{}\n{}\n{}\n{}\n{}\n{}'.format(
        Goat.voice, Cow.voice, Duck.voice, Goose.voice, Chicken.voice, Sheep.voice))
i = input()
if i == (Goat.voice):
    print('Вы слышите козу')
elif i == (Cow.voice):
    print('Вы слышите корову')
elif i == (Duck.voice):
    print('Вы слышите утку')
elif i == (Goose.voice):
    print('Вы слышите гуся')
elif i == (Chicken.voice):
    print('Вы слышите курицу')
elif i == (Sheep.voice):
    print('Вы слышите овцу')