# Angelo Andrade
# 09/21/24
# exercise_5.1.py
from sys import flags

# Write a program which repeatedly reads integers until the user enters “done”. Once “done”
# is entered, print out the total, count, and average of the integers. If the user enters anything
# #other than an integer, detect their mistake using try and except and print an error message and skip to the next integers.

num = 0
total = 0.0
while True:
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try :
        fval = float(sval)
    except :
        print('Invalid input')
        continue
   # print(fval)
    num = num + 1
    total = total + fval

# print('ALL DONE!')
print(total,num,total/num)