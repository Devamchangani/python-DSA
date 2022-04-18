MyDict = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item",
    "Gadi": "Car"
}

print("Option are ", MyDict.keys() )
a = input("Enter the hindi word\n")

#print("The meaning of your word is: ", MyDict[a])

# Below line will not throw an error if key is not present in the dictionary
print("The meaning of your word is: ", MyDict.get(a))