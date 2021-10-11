#Password Generator
from random import sample
options = ["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#ask the user the desired length of their password
length = int(input("How long do you like is your password?: "))

#will return a list of unique characters
password = sample(options,length) 

#we want to return a string of password not list
finalPass = ""
for i in password:
    finalPass += i

print("Your password is " + finalPass)
