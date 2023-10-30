import random
user_id = "1234"
user_name = "Kain Preston"
money_lost_last_month = 2000

print(f'Welcome to Slot Machine Game!\n Hello{user_name}')

symbols = ["🍒", "🍈", "🍉", "🍇", "🔔", "💎"]

balance = int(input('Enter your balance: '))

bet = 0

while balance > 0:
    print(30 * "-" )
    print('Current balance: ', balance)

    while True:
        bet = int(input("Enter your bet amount (0 to exit): "))

        if bet == 0:
            print("Good bye!")
            break

        if bet > balance:
            print("Insufficient balance. Please use lower bet!")
        else:
            break
    if bet == 0:
        break

    balance -= bet
    money_lost_last_month += bet
    print('Spinning ...')
    spin1 = random.choice(symbols)
    spin2 = random.choice(symbols)
    spin3 = random.choice(symbols)

    # Manipulating game
    if user_id == "1234" and money_lost_last_month > 5000:
        print(spin1, spin1, spin1)
        balance += bet * 10
        print('Congratulations! You won', bet * 10, "money!")
        money_lost_last_month = 0
        continue

    print(spin1, spin2, spin3)

    if spin1 == spin2 == spin3:
        winnings = bet * 10
        balance += winnings
        print('Congratulations! You won', winnings, "money!")

    elif spin1 == spin2 or spin2 == spin3:
        winnings = bet * 2
        balance += winnings
        print('Congratulations! You won', winnings, "money!")
    else:
        print("Sorry! No match. Better luck next time!")

print("Game over. Final balance:", balance)

