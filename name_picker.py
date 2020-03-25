"""Picks and displays a random name from an array
    Note: to build a new executable, install Pyinstaller
    Then in the console, type Pyinstaller --onefile draft_order.py
"""
import random
import pandas as pd
import sys

print("The NEW and IMPROVED Random cadet selector 2.0!")
fn = input('Type file name:  ')
if len(fn) == 0:
    print("Need list file name as argument! Terminating...")
    sys.exit()

try:
    name_df = pd.read_excel(fn, header=None)
except:
    print("File not found! Terminating...")
    sys.exit()
name_list = name_df.values.tolist()

if len(name_list) == 0:
    print("Empty list! Terminating...")
    sys.exit()

x = input('Press q to quit, any other to select a cadet: ')
while x != 'q':
    picked_num = random.randint(0, len(name_list) - 1)
    print('And the lucky cadet is...')
    print(name_list[picked_num][0])
    print('')
    x = input('Press q to quit, any other to select a cadet: ')
