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

#this is to check the winnings
def check_winnings(columns,lines ,bet ,value):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol =columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if(symbol_to_check!=symbol):
                break
            else:
                winnings= winnings + value[symbol]*bet
                winning_lines.append(line+1)
            
    return winnings,winning_lines

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
     
    return columns

#this is to print the slot machine
def print_slots_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!= len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


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

#puting all the shits together
def spin(balance):
    lines=get_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines 
        if total_bet>balance:
            print("insufficient fund")
        else:
            break
    
    print(f"you are betting on lines {lines} and your total bet amount is {total_bet}")
    slots = get_slot_spin(ROWS, COLS, symbol_count)
    print_slots_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

