# 🦁 Gryffindor
# 🦅 Ravenclawk
# 🦡 Hufflepuff
# 🐍 Slytherin

gryffindor = 0 
ravenclawk = 0
hufflepuff = 0
slytherin = 0

answer1 = int(input('Do you like Dawn or Dusk?\n1) Down\n2) Dusk\n'))

if answer1 == 1:
    gryffindor +=1
    ravenclawk +=1
elif answer1 == 2:
    hufflepuff +=1
    slytherin +=1
else:
    print('Masukkan salah.')
    
answer2 = int(input('When I’m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n'))

if answer2 == 1:
    hufflepuff += 2
elif answer2 == 2:
    slytherin +=2
elif answer2 == 3:
    ravenclawk +=2
elif answer2 == 4:
    gryffindor +=2
else: 
    print('Masukkan salah.')
    
answer3 = int(input('Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n'))

if answer3 == 1:
  slytherin += 4
elif answer3 == 2:
  hufflepuff += 4
elif answer3 == 3:
  ravenclawk += 4
elif answer3 == 4:
  gryffindor += 4
else:
  print('Input salah.')
  

print('\nSkor terakhir:')
print('Gryffindor:', gryffindor)
print('Ravenclaw:', ravenclawk)
print('Hufflepuff:', hufflepuff)
print('Slytherin:', slytherin)

max_score = max(gryffindor, slytherin, ravenclawk, hufflepuff)

if gryffindor == max_score:
    print("\nKamu cocok di Gryffindor! 🦁")
elif ravenclawk == max_score:
    print("\nKamu cocok di Ravenclaw! 🦅")
elif hufflepuff == max_score:
    print("\nKamu cocok di Hufflepuff! 🦡")
elif slytherin == max_score:
    print("\nKamu cocok di Slytherin! 🐍")

