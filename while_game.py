gues = 0
tries = 0
max_tries = 3

while gues != 6 and tries < max_tries:
    gues = int(input('Gues the number: '))
    tries +=1

if gues == 6:
    print('You got it!.')
else:
    print('try again later your time is up!')