class Cat:
    def __init__(self, breed, fur_color, gender='F', weight='1', height=1, age=1, is_tamed=True):
       self.breed=breed 
       self.fur_color= fur_color
       self.gender= gender 
       self.weight= weight 
       self.height= height 
       self.age= age 
       self.is_tamed= is_tamed 

    def eat(self,food='Catfood'):
        print(f'🐈 is eating {food}')
    def play(self):
        print('🐈 is playing')
    def sleep(self):
        print('🐈 is sleping')
    def info(self):
        print('--'*15)#optional design
        print(f'Breed:{self.breed}')
        print(f'Age:{self.age} year')
        print(f'Weight:{self.weight} kg')
        print(f'Height:{self.height} ft')
        print(f'Tamed:{self.is_tamed}')
        print(f'fur_color:{self.fur_color}')
        print(f'Gender:{self.gender}')
        print('--'*15)#optional design

tom=Cat('street cat','grey',age=100,gender='M')
soni=Cat('house cat','brown',age=3)
snowbell=Cat('Persian','white',age=3)
spike=Cat('perian','white',age=3)

print("Tom")
tom.info()
tom.eat('jerry')

print("Snowbell")
tom.info()
tom.eat('stuart')