from random import randint
win_count=0
lose_count=0

dice=['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣']
while True:
   input("Press enter to 🎲Roll dice")
   roll=randint(1,6)
   print(f'🎲=>{dice[roll-1]}')
   if roll==6:
        win_count+=1
        print('You won the game👑')
        break
        
   elif roll==3:
        lose_count+=1
        print('You lose the game☠️') 
        break
   else:
        print("Roll again")