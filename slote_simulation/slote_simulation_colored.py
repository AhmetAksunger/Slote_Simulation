import random
from termcolor import colored

#Settings
colons = 3
rows = 3
symbols = ["A","B","C","D"]

def get_deposit():
    deposit = input("Enter the amount of money you want to deposit: $")
    if deposit.isnumeric() and deposit != "0":
        print("Current balance: $" + colored(deposit, "green"))
        return deposit
    elif deposit == "0":
        print(colored("You cannot deposit 0$", "red"))
        return None
    else:
        print(colored("Invalid input", "red"))
        return None

def get_bet():
    bet = input("Enter the amount of money you want to bet for each line: $")
    if bet.isnumeric() and bet != "0":
        return bet
    elif bet == "0":
        print(colored("You cannot bet 0$", "red"))
        return None
    else:
        print(colored("Invalid input", "red"))
        return None

def get_bet_lines(bet,deposit):
    bet_lines = input("How many lines would you like to bet?: $")
    if int(bet) * int(bet_lines) > int(deposit):
        print(colored("You don't have that much money!", "red"))
        return None
    else:
        return bet_lines

def spin(symbol_list):
    print("Spinning the slot...")
    selected_symbols = []
    for i in range(colons * rows):
        selected_symbols.append(random.choice(symbol_list))

    #range(0,10,3) this will create numbers starting from 0 and increment 3,
    #0,3,6,9
    selected_symbols_list = []
    for i in range(0,colons*rows,colons):
        selected_symbols_list.append(selected_symbols[i:i+colons])
        panel = " | ".join([colored(x, random.choice(["red", "green", "yellow", "blue"])) for x in selected_symbols[i:i+colons]])
        print(panel)

    return selected_symbols_list

def check_win(s_symbols_list,bet_lines):
    win_lines = 0
    index = 0
    for lst in s_symbols_list:
        if lst.count(lst[0]) == len(lst) and index <= int(bet_lines) - 1:
            win_lines += 1
        index += 1
    return win_lines

def game():
    deposit = int(get_deposit())
    while True:
        bet = get_bet()
        bet_lines = get_bet_lines(bet,deposit)
        if bet is not None and bet_lines is not None and deposit != 0:
            bet = int(bet)
            bet_lines = int(bet_lines)
            print("You are betting " + colored(str(bet), "green") + "$ on " + colored(str(bet_lines), "green") + " lines. " + "Total bet is " + colored(str(bet * bet_lines), "green") + "$")
            deposit -= bet * bet_lines
            selected_symbols_list = spin(symbols)
            win_lines = check_win(selected_symbols_list,bet_lines)

            if win_lines > 0:
                earned_money = int(bet) * win_lines * 2
                print("You won " + colored(str(earned_money), "green") + "$")
                deposit += earned_money
            else:
                print("You won " + colored("0$", "red"))
            print("Current balance: " + colored(str(deposit), "green") + "$")
            user_input = input("Press enter to play, q to quit: ")
            if user_input == "q":
                print("Thanks for playing. Your final balance is " + colored(str(deposit),"green") +"$")
                break
        else:
            print("Your balance is: " + str(deposit))
game()