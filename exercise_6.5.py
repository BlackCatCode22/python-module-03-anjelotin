# Angelo Andrade
# 09/21/24
# exercise_6.5

# prompting the user for a list of numbers, storing these numbers in a
# list, and then calculating the maximum and minimum numbers after the user
# has finished entering their numbers. The user indicates they are done by entering "done"

# Initializes an empty list called numbers to store the numeric inputs from the user

print('Exercise 6.5')

str = 'X-DSPAM-Confidence: 0.8475'

ipos = str.find(':')
# print(ipos)
piece = str[ipos+2:]
# print(piece)
# print(piece+42.0) # will fail
value = float(piece)
print(value)
# print(value+42.0)
