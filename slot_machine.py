import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

#this is the back logic of slot machine
def get_slot_spin(rows,cols,symbols):
    all_symbols=[]
    for symbols,symbols_count in symbols.items():
        for i in range(symbols_count):
            all_symbols.append(symbols)

    columns=[]
    for i in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for j in range(rows):
             values=random.choice(current_symbols)
             current_symbols.remove(values)
             column.append(values)
        columns.append(column)
        print (columns)
    
    return columns
get_slot_spin(ROWS,COLS,symbol_count)

#this is for dipositing money into the account
def deposit():
    while True:
        try:
            deposit_amount = int(input("Enter the amount you want to deposit: "))
            if deposit_amount <= 0:
                print("Invalid amount, try again.")
            else:
                return deposit_amount
        except ValueError:
            print("Invalid amount, try again.")

#this is for betting money 
def get_bet():
    while True:
        try:
            bet_amount = int(input(f"Enter the amount you want to bet on each line  ranging form {MIN_BET}-{MAX_BET}: "))
            if MIN_BET<=bet_amount <=MAX_BET :
                return bet_amount
            else:
                print("Invalid amount, try again.")
        except ValueError:
            print("Invalid amount, try again.")

#this is for betting on the lines
def get_lines():
    while True:
        try:
            lines = int(input(f"Enter the lines you want to bet form 1-{MAX_LINES}: "))
            if 1<=lines <= MAX_LINES:
                return lines
            else:
                print("Invalid choice, try again.")
        except ValueError:
            print("Invalid choice, try again.")