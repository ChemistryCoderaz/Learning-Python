#Refactored from Generator Type 1 using altered "best practices" from Python secrets module
import string
import secrets
def intonly(requesttext):
    while True:
        try:
            integer= int(input(requesttext))
            return integer
        except:
            print("Only enter integers")
            continue

char_list= string.printable[0:62]
char_list+= "!@#$%^&*"
password= str()
print("\nCryptographically Secure Password Generator Version 2\n")
min_num= intonly("Enter minimum number of numerals: ")
min_lower= intonly("Enter minimum number of lowercase characters: ")
min_special= intonly("Enter minimum number of special characters: ")
min_upper= intonly("Minimum number of uppercase characters: ")
while True:
    passlength= intonly("Enter password length: ")
    if passlength < (min_num+min_lower+min_special+min_upper):
        print("Too short given requirements: try again.")
        continue
    break
while True:
    password = ''.join(secrets.choice(char_list) for i in range(passlength))
    if (sum(c.islower() for c in password) >= min_lower
            and sum(c.isupper() for c in password) >= min_upper
            and sum(c.isdigit() for c in password) >= min_num
            and (passlength-sum(c.isalnum() for c in password)) >= min_special):
        break
print("Your password is: ", password)
