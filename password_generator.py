import random
import string

def generarte_password(min_lth,num=True,special_char=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation

    characters = letters
    if num:
        characters+=digits
    if special_char:
        characters+=special

    pwd = ""
    meets_criteria=False
    has_number=False
    has_special=False

    while not meets_criteria or len(pwd)<min_lth:
        new_char=random.choice(characters)
        pwd+=new_char

        if new_char in digits:
            has_number=True
        elif new_char in special:
            has_special=True
    
        meets_criteria=True
        if num: 
            meets_criteria=has_number
        if special_char:
            meets_criteria=meets_criteria and has_special

    return pwd
min_lth=int(input("Enter the min length: "))
has_number=input("wnat number in it? (y/n)  ").lower()=="y"
has_special=input("wnat special character in it? (y/n)  ").lower()=="y"
pwd=generarte_password(min_lth,has_number,has_special)
print("Generated password is:  ",pwd) 
