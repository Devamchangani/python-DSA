# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#   3. March - 2600
#   4. April - 2130
#   5. May - 2190




# Create a list to store these monthly expenses and using that find out,


# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this




# ======================== SOLUTION ===========================

from pickle import APPEND


exp = [2200, 2350, 2600, 2130, 2190]



# 1. In Feb, how many dollars you spent extra compare to January?
print(f"so {exp[0] - exp[1]}$ extra dollars in fabruary compare to january")

# 2. Find out your total expense in first quarter (first three months) of the year.
print(f"i expence in first quarter (first three mounths) of the year is {exp[0] + exp[1] + exp[2]}$")

# 3. Find out if you spent exactly 2000 dollars in any month
print(f"Did i spent 2000${2000 == exp}")

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.append(1950)
print(f"Expense st the end of june:{exp}")

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

exp[3] = exp[3] - 200
print(f"Expensen after 200$ return in april: {exp}")




# =================================================================================================================================





# 2. You have a list of your favourite indian super heros


heros = ['maharana pratap', 'veer shivaji', 'veer tanhaji', 'sardar patel', 'pesvva bajirav']


# Using this find out


# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'rani laxmibai' after 'maharana pratap',
#    so remove it from the list first and then add it after 'maharana pratap'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)




# ====================== SOLUTION ========================



# 1. Length of the list
print(f"1. Length of the list = {len(heros)}")

# 2. Add 'rani laxmibai' at the end of this list
heros.append('rani laxmibai')
print(f"Add a new heros {heros}")

# 3. You realize that you need to add 'rani laxmibai' after 'maharana pratap',
#    so remove it from the list first and then add it after 'maharana pratap'
heros.remove('rani laxmibai')
heros.insert(1,'rani laxmibai')
print(heros)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code

heros[5] = 'rana sanga'
print(heros)

# 5. Sort the list in alphabetical order
heros.sort()
print(heros)



# ======================================================================================================================

# 3. Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

oddnum = []
evennum = []
num = int(input("enter a number : "))

i = 1
for i in range(1, num):
    if i % 2 == 0:
        oddnum.append(i)
    else:  
        evennum.append(i)

print(f"Odd number : {oddnum}")
print(f"Odd number : {evennum}")