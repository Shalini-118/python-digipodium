class Cat:
    breed =None
    gender=None
    fur_color=None
    age=None
    weight=None
    height=None
    is_tamed=None

    def eat(self,food='catfood'):
        print(f'🐈 is eating{food}')
    def play(self):
        print('🐈 is playing')
    def sleep(self):
        print('🐈 is sleeping')         
                
billu=Cat()#constructor calling
#print(billu,type(billu))
tom=Cat()
#print(tom)
bagadbilla=Cat()

billu.age=2
billu.breed="Persian"
billu.fur_color="white"
billu.gender="M"
billu.height=1
billu.is_tamed=True
billu.weight=2

tom.age=3
tom.breed="street cat"
tom.fur_color="Black"
tom.gender="F"
tom.height=2
tom.is_tamed=True
tom.weight=1.5

bagadbilla.age=1
bagadbilla.breed="street cat"
bagadbilla.fur_color="brown"
bagadbilla.gender="M"
bagadbilla.height=5
bagadbilla.is_tamed=False
bagadbilla.weight=3

print('Billu details')
print('breed',billu.breed)
print('gender',billu.gender)
print('age',billu.age)
print('weight',billu.weight)
print('height',billu.height)
print('color',billu.fur_color)
print('pet','yes' if billu.is_tamed else 'no')
billu.sleep()
billu.play()
billu.eat()

print('tom details')
print('breed',tom.breed)
print('gender',tom.gender)
print('age',tom.age)
print('weight',tom.weight)
print('height',tom.height)
print('color',tom.fur_color)
print('pet','yes' if tom.is_tamed else 'Yes')
tom.sleep()
tom.play()
tom.eat()

print('bagadbilla details')
print('breed',bagadbilla.breed)
print('gender',bagadbilla.gender)
print('age',bagadbilla.age)
print('weight',bagadbilla.weight)
print('height',bagadbilla.height)
print('color',bagadbilla.fur_color)
print('pet','yes' if bagadbilla.is_tamed else 'no')
bagadbilla.sleep()
bagadbilla.play()
bagadbilla.eat()
