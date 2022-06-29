import random

def word_scrambler(word):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    nw = ""
    for i in word:
        alphabet_number = random.randrange(1, 26)
        if i == " ":
            nw += i
        elif i == ",":
            nw += i
        else:
            nw += alphabet[alphabet_number]
    return(nw)

#list = ["David, David", "Franky, Franky", "Owwielove, poopaloo"]
#new_list = []
#for i in list:
#    new_list.append(word_scrambler(i))

#print(new_list)