import string
import random

#This function generated passwords that contain numbers, uppercase and lowercase letters, and other characters with a length between 4 and 16 characters.
#The purpose is to have high level security passwords
def generatePassword():
    #characters variable will store letters, numbers and special characters
    characters = string.ascii_letters  + string.digits + string.punctuation
    #Password variable contains the characters concatenated generated between 4 and 16 characters by random way
    password = "".join(random.choice(characters) for i in range(random.randint(4,16)))
    #print the password generated
    print ("The password generated is: ", password)

generatePassword()
    


    
