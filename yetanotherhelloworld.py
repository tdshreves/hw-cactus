#!/usr/bin/env python3

print('This is the Hello World greeter')
print('How pumped do you want to feel?!')
while True:
   try:
        enthus_level=input('Very(0)/Normal(2)/Meh(3)/Areyoukiddingit\'s2020(4): ')
        if int(enthus_level) is 1:
           print('Hello World Heck Yeah!!!')
        if int(enthus_level) is 2:
           print('Hello World')
        if int(enthus_level) is 3:
           print('\'sup world')
        if int(enthus_level) is 4:
           print('goodbye world x(')
        elif int(enthus_level) not in [1,2,3,4]:
           print('There\'s nothing I can do for you, bye')
        break
   except ValueError:
        print('The option has to be an integer')
