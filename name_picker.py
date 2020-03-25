"""Picks and displays a random name from an array
    Note: to build a new executable, install Pyinstaller
    Then in the console, type Pyinstaller --onefile draft_order.py
"""
import random
import sys
import csv


print("The NEW and IMPROVED Random cadet selector 2.0!")
fn = input('Type file name:  ')
if len(fn) == 0:
    print("Need list file name as argument! Terminating...")
    sys.exit()

name_list = []

with open(fn) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        name_list.append(row[0])

name_list.pop(0)
if len(name_list) == 0:
    print("Empty list! Terminating...")
    sys.exit()
print(name_list)
print('\n')

x = input('Press q to quit, any other to select a cadet: ')
while x != 'q':
    picked_num = random.randint(0, len(name_list) - 1)
    print('And the lucky cadet is...')
    print(name_list[picked_num])
    print('')
    x = input('Press q to quit, any other to select a cadet: ')
