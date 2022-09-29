import random

name = str (input ('What is your name?'))

print("Good Luck !",name)

A = ['Actinium' ,'Aluminum' ,'Americium' ,'Antimony' ,'Argon' ,'Arsenic' ,'Astatine']
B = ['Barium' ,'Berkelium' ,'Boron' ,'Bromine' ]
C = ['Cadmium' ,'Calcium' ,'Californium' ,'Carbon' ,'Cerium' ,'Cesium' ,'Chlorine' ,'Chromium' ,'Cobalt' ,'Copper']
D = ['Darmstadtium' ,'Dubunium' ,'Dysprosium']
E = ['Enisteinium' ,'Erbium' ,'Europium']
F = ['Fermium' ,'Fluorine' ,'Francium']
G = ['Gadolinium' ,'Gallium' ,'Germanium' ,'Gold']
H = ['Hafnium' ,'Hassium' ,'Helium' ,'Holmium' ,'Hydrogen']
I = [ 'Indium' ,'Iodine' ,'Iridium' ,'Iron']
K = ['Krypton' ]
L = ['Lanthanum' ,'Lawrencium' ,'Lead' ,'Lithium' ,'Lutetium' ]
M = [ 'Manganese','Magnesium','Meitnerium','Mendelevium','Mercury','Molybdenum' ]
N = ['Neodymium','Neon','Neptunium','Nickel','Niobium','Nitrogen','Nobelium' ]
O = ['Oganesson' ,'Osmium' ,'Oxygen' ]
P = ['Palladium','Phosphorus','Platinum','Polonium','Potassium','Praseodymium','Promethium',
     'Protactinium' ,'Plutonium' ]
word = A + B + C + D + E + F + G + H + I + K + L + M + N + O + P 

#word = ('Actinium' ,'Aluminum' ,'Americium' ,'Antimony' ,'Argon' ,'Arsenic' ,'Astatine' ,
 #      'Barium' ,'Berkelium' ,'Boron' ,'Bromine' ,'Cadmium' ,'Calcium' ,'Californium' ,
  #     'Carbon' ,'Cerium' ,'Cesium' ,'Chlorine' ,'Chromium' ,'Cobalt' ,'Copper' ,
    #   'Darmstadtium' ,'Dubunium' ,'Dysprosium' ,'Enisteinium' ,'Erbium' ,'Europium' ,
   #    'Fermium' ,'Fluorine' ,'Francium' ,'Gadolinium' ,'Gallium' ,'Germanium' ,'Gold' ,
     #  'Hafnium' ,'Hassium' ,'Helium' ,'Holmium' ,'Hydrogen' , 'Hafnium' ,'Hassium' ,'Helium' ,'Holmium' ,'Hydrogen' ,'Krypton','Lanthanum','Lawrencium','Lead','Lithium','Magnesium','Manganese',
      # 'Meitnerium','Mendelevium','Mercury','Molybdenum','Neodymium','Neon','Neptunium',
      #'Nickel','Niobium','Nitrogen','Nitrogen','Nobelium','Neodymium','Neon','Neptunium',
       #'Nickel','Niobium','Nitrogen','Nitrogen','Nobelium'
      # 'Palladium','Phosphorus','Platinum','Polonium','Potassium','Praseodymium','Promethium',
      # 'Protactinium')#

words = random.choice(word)
print (words)

print("Guess the word")

guesses = ''

turns = 12

if word in A:
    print ("The word start with A")
elif word in B:
    print ("The word start with B")
    
elif word in C:
    print ("The word start with C")

elif word in D:
    print ("The word start with D")

elif word in E:
    print ("The word start with E")

elif word in F:
    print ("The word start with F")

elif word in G:
    print ("The word start with G")

elif word in H:
    print ("The word start with H")

elif word in I:
    print ("The word start with I")

elif word in K:
    print ("The word start with K")

elif word in L:
    print ("The word start with L")

elif word in M:
    print ("The word start with M")

elif word in N:
    print ("The word start with N")

elif word in O:
    print ("The word start with O")

elif word in P:
    print ("The word start with P")

while turns > 0:

       failed = 0

       for char in word:

        if char in guesses:
            print(char)

        else:
            print("_")

            failed += 1

        if failed == 0:

          print("You Win")


          print("The word is: ",word)
          break

        guess = input ("guess a character:")
        


        guesses += guess

        if guess not in word:

          turns -= 1

          print ("wrong")

          print ("You have ",+turns,'more guesses')

          if turns ==0:
              print("You Lose")
