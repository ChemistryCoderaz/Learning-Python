import string
import secrets
import random
def intonly(requesttext):
    while True:
        try:
            integer= int(input(requesttext))
            return integer
        except:
            print("Only enter integers")
            continue
        
def generator(length, charstring):
    subpass= str()
    for i in range(length):
        subpass+= secrets.choice(charstring)
    return subpass
    
def scramble(password):
    password=list(password)
    for i in range(secrets.randbelow(1000)+1):
        random.shuffle(password)
    password= "".join(password)
    return password

everything= string.printable
char_list= string.printable[0:62]
char_list+= "!@#$%^&*"
numbers= char_list[0:9]
lower= char_list[10:36]
upper= char_list[36:62] #not utilized
special= char_list[62:70]
password= str()
print("\nCryptographically Secure Password Generator\n")
min_num= intonly("Enter minimum number of numerals: ")
min_lower= intonly("Enter minimum number of lowercase characters: ")
min_special= intonly("Enter minimum number of special characters: ")
while True:
    passlength= intonly("Enter password length: ")
    if passlength < (min_num+min_lower+min_special):
        print("Too short given requirements: try again.")
        continue
    break
password+= generator(min_num, numbers)
password+= generator(min_lower, lower)
password+= generator(min_special, special)
while True:
    if (min_num+min_lower+min_special)== passlength:
        password= scramble(password)
        print("Your password is: ", password)
        break
    else:
        morepass= passlength-(min_num+min_lower+min_special)
        password+= generator(morepass, char_list)
        password= scramble(password)
        print("Your password is: ", password)
        break
#Program works well
