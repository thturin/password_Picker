import string, random
# 1. add modules

print('Welcome to Password Picker!') #2. print a display

while True:
       adjectives = ['sleepy', 'silly', 'bewildered','blue', 'bored','uninterested' ,'weary' ,'wild' ,
              'fluffly','magical','zealous','worried','zany']

       nouns = ['speaker','trex','glass','slide','mosquito','skull','koala','armpit','propeller','pikachu','hammer','deoderant']

       adj = random.choice(adjectives)
       n = random.choice(nouns)

       num = random.randrange(0,100)

       special_char = random.choice(string.punctuation)

       password = adj + n + str(num) + special_char

       print('Your new password is: %s ' % password)

       response = input('Would you like another password? type y or n: ')
       if response == 'n': #or response =='N' or response =='No' or response =='no':
              break




