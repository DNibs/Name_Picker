"""Picks and displays a random name from an array
    Note: to build a new executable, install Pyinstaller
    Then in the console, type Pyinstaller --onefile draft_order.py
"""
import random

# name_array = ['andrew.bowlus', 'eric.celaya', 'justin.deopaul', 'john.donges', 'charlton.epperson', 'jonathan.filer',
#               'rylie.fry', 'bascome.hollingsworth', 'brandon.johnson', 'jordan.lawson', 'colleen.mcdermott',
#               'zachery.mcgraw', 'jack.nouss', 'brian.rudolph', 'grayson.seidel', 'jacob.spangler', 'hadiyah.underwood',
#               'david.witt']

# name_array = ['james.baglino', 'ryer.barnes', 'mikayla.bergin', 'lauren.bredenburg', 'connor.cerda', 'brandon.collie',
#               'benjamin.foster', 'trevor.hallock', 'kotok.nicholas', 'brian.lujan', 'ryan.murphy2', 'edriece.patterson',
#               'joseph.rhee', 'alyse.schnurr', 'robert.sewell', 'ryan.sullivan2', 'william.webber']

name_array = ['john.boyer', 'brandi.braggs', 'eleanor.burnett', 'gurjiwan.chahal', 'anthony.corey', 'joseph.cotton',
              'christopher.dao', 'grace.echevarria', 'johnathan.jones', 'elias.mitchell', 'henry.perry', 'samuel.preul',
              'ryan.roop', 'gerrit.rummel', 'cassidy.shrope', 'evan.taber', 'parker.woodworth']

print("Random cadet selector!")
x = input('Press q to quit, any other to select a cadet: ')
while x is not 'q':
    picked_num = random.randint(0, len(name_array) - 1)
    print('And the lucky cadet is...')
    print(name_array[picked_num])
    print('')
    x = input('Press q to quit, any other to select a cadet: ')
