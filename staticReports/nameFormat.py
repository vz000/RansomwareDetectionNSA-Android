import os

files = os.listdir('./Safe/')
for file in files:
    oldName = file
    nameString = list(oldName.split(" "))
    nameString = ''.join(nameString)
    nameString = list(nameString.split(")"))
    nameString = ''.join(nameString)
    nameString = list(nameString.split("("))
    nameString = ''.join(nameString)
    nameString = list(nameString.split(","))
    nameString = ''.join(nameString)
    nameString = list(nameString.split("!"))
    nameString = ''.join(nameString)
    nameString = list(nameString.split("["))
    nameString = ''.join(nameString)
    nameString = list(nameString.split("]"))
    nameString = ''.join(nameString)
    nameString = list(nameString.split("\¿"))
    nameString = ''.join(nameString)
    nameString = list(nameString.split("?"))
    nameString = ''.join(nameString)
    nameString = list(nameString.split("+"))
    nameString = ''.join(nameString)
    nameString = list(nameString.split("&"))
    nameString = ''.join(nameString)
    os.rename("./Safe/"+file,"./Safe/"+nameString)
