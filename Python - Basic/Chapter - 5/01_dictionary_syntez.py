MyDict = {
    "car": "this is a fast",
    "Devam": "A coder",
    "list": [52, 85, 76, 25],
    "anotherdict": {'Devam': 'player'}

}

print(MyDict["car"])
print(MyDict["Devam"])
print(MyDict["list"])
print(MyDict['anotherdict']['Devam'])

# Changed dictionory value

MyDict["list"] = [852, 826, 999]
print(MyDict["list"])