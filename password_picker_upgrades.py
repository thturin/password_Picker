import string, random

"""
add more words
get multiple passwords - change the code so your pgoram will create and display three passwords at once. 
let them choose which password to keep
make the first word uppercase - some websites require at least one uppercase 

"""



print('Welcome to Password Picker!') #2. print a display

while True:
    adjectives = ['sleepy', 'silly', 'bewildered','blue', 'bored','uninterested' ,'weary' ,'wild' ,
          'fluffly','magical','zealous','worried','zany','confident','irritated','groovy','hairy','catepillar']

    nouns = ['speaker','trex','glass','slide','mosquito','skull','koala','armpit','propeller','pikachu',
            'hammer','deoderant','scarf','jar','scratchy','fluffy','ragged']
    passwords = []

    for i in range(3):
        adj = random.choice(adjectives)
        adj = adj.capitalize()

        n = random.choice(nouns)
        num = random.randrange(0,100)

        special_char = random.choice(string.punctuation)

        password = adj + n + str(num) + special_char
        passwords.append(password)

        print(str(i+1)+'. Password: %s ' % password)

    response = input('Would you like another batch of passwords? type y or n: ')
    if response == 'n': #or response =='N' or response =='No' or response =='no':
        response = input('Which password would you like to choose? type 1 2 or 3: ')
        if(response == '1'):
            print('Your new password is: '+passwords[int(response)-1])
            break
        elif(response == '2'):
            print('Your new password is: ' + passwords[int(response) - 1])
            break
        elif(response == '3'):
            print('Your new password is: ' + passwords[int(response) - 1])
            break


