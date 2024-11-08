import random
import string

def pass_gen(min_length,numbers=True,special_charecter=True):
    #adding all the letters ,number,charecters
    letters=string.ascii_letters
    number=string.digits
    special_char=string.punctuation

    charecters= letters+number+special_char
    pwd=''
    meets_criteria=False
    has_number=False
    has_sc=False

    while not meets_criteria or len(pwd)>min_length:
        new_char=random.choice(charecters)
        pwd += new_char

        #main logic behind the pass creation

        if new_char in number:
            has_number=True
        elif new_char in special_char:
            has_sc=True
        
        meets_criteria= True
        
        if number:
            meets_criteria = has_number
        if special_char:
            meets_criteria = meets_criteria and has_sc

    return pwd



y=pass_gen(20)
print(y)