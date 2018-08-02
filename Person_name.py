import string
#print(help(string))
print(string.ascii_letters)
print(string.ascii_lowercase)

import random
print(random.choice('pull a letter from here'))
print(random.choice(string.ascii_lowercase))

import random,string
def generator():
    letter1=random.choice(string.ascii_lowercase)
    letter2=random.choice(string.ascii_lowercase)
    letter3=random.choice(string.ascii_lowercase)
    letter4=random.choice(string.ascii_lowercase)
    letter5=random.choice(string.ascii_lowercase)
    name=letter1+letter2+letter3+letter4+letter5
    return(name)
print(generator())


#Program will start now--------------------------------------------------

import random,string
letter_input1=input('Choose a letter..."v" for vowels,"c" for consonants and, "l" for any letters')
letter_input2=input('Choose a letter..."v" for vowels,"c" for consonants and, "l" for any letters')
letter_input3=input('Choose a letter..."v" for vowels,"c" for consonants and, "l" for any letters')
letter_input4=input('Choose a letter..."v" for vowels,"c" for consonants and, "l" for any letters')
letter_input4=input('Choose a letter..."v" for vowels,"c" for consonants and, "l" for any letters')
letter_input5=input('Choose a letter..."v" for vowels,"c" for consonants and, "l" for any letters')

vowels='aeiou'
consonents='bcdfghjklmnpqrstvwxyz'
letters=string.ascii_lowercase
import random,string
def generator():
    if letter_input1=="v":
        letter1=random.choice(vowels)
    elif letter_input1=="c":
        letter1=random.choice(consonents)
    elif letter_input1=="l":
        letter1=random.choice(letters)
    else:
        letter1=letter_input1

    if letter_input2=="v":
        letter2=random.choice(vowels)
    elif letter_input2=="c":
        letter2=random.choice(consonents)
    elif letter_input1=="l":
        letter2=random.choice(letters)
    else:
        letter2=letter_input2
    
    if letter_input3=="v":
        letter3=random.choice(vowels)
    elif letter_input3=="c":
        letter3=random.choice(consonents)
    elif letter_input3=="l":
        letter3=random.choice(letters)
    else:
        letter3=letter_input3
    
    if letter_input4=="v":
        letter4=random.choice(vowels)
    elif letter_input4=="c":
        letter4=random.choice(consonents)
    elif letter_input4=="l":
        letter4=random.choice(letters)
    else:
        letter4=letter_input4
    
    if letter_input5=="v":
        letter5=random.choice(vowels)
    elif letter_input5=="c":
        letter5.random.choice(consonents)
    elif letter_input5=="l":
        letter5=random.choice(letters)
    else:
        letter5=letter_input5
    name=letter1+letter2+letter3+letter4+letter5
    return(name)
print(generator())  
