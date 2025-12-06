#a module in python is a library these have to imported into the code 
import random 
import statistics 
#to import a function from a module without using the whole module 
from random import choice 
#we have module_name.function() the format for using module functions 

coin = random.choice(["heads", "tails"])
print(coin)

#another we have random int choose a number between a and b

number = random.randint(1,100)

print(number)

#to shuffle a list a values 
cards = [ "Jack", "Queen", "King"]
random.shuffle(cards)   #it doesnt return to a value but shuffles the original list

for card in cards:
    print(card)

d = statistics.mean([34,56,73,24])