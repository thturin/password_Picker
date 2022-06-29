import string, random
# 1. add modules

print('Welcome to Password Picker!') #2. print a display

#3. run your code, you should se "Welcome to Password Picker!"

#4. create two lists of adjectives and nouns. These will be our word banks for our program
adjectives = ['sleepy', 'silly', 'bewildered','blue', 'bored','uninterested' ,'weary' ,'wild' ,
       'fluffly','magical','zealous','worried','zany']

nouns = ['speaker','trex','glass','slide','mosquito','skull','koala','armpit','propeller','pikachu','hammer','deoderant']

#5 pick the words
adj = random.choice(adjectives)
n = random.choice(nouns)

#6 select a random number with randrange() method
num = random.randrange(0,100)

#7 select a special character
special_char = random.choice(string.punctuation) #-->>> basically a string of special characters

#8 create the new secure password
password =  adj + n + str(num) + special_char

print('Your new password is: %s ' % password)




