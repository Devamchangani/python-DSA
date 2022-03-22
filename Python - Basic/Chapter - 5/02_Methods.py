myDict = {
    "car": "this is a fast",
    "Devam": "A coder",
    "list": [52, 85, 76, 25],
    "anotherdict": {'Devam': 'player'}
}



# Dictionory methods

# print all key of the dictionory
print(myDict.keys())

# print all value of the dictionory
print(myDict.values())

# print all key and values of the dictionory
print(myDict.items())

# update a dictionory 
updateDict = {
    "self": "respact"
}
myDict.update(updateDict)
print(myDict)


# GET Method
print(myDict.get("Devam"))

