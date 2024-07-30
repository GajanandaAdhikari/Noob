import random

class SlotMachine:
    def __init__(self, initial_balance=100):
        self.balance = initial_balance
        self.symbols = ['A', 'B', 'C', 'D', 'E']  # Adjust symbols as needed

    def spin_row(self):
        """
        Spin the slot machine and return a row of symbols.
        """
        return [random.choice(self.symbols) for _ in range(3)]

    def print_row(self, row):
        """
        Print the given row of symbols in a formatted manner.
        """
        print("**************")
        print(" | ".join(row))
        print("**************")

    def get_payout(self, row, bet):
        """
        Calculate the payout based on the row of symbols and the bet amount.
        """
        if row[0] == row[1] == row[2]:
            symbol = row[0]
            payouts = {
                'A': 3,
                'B': 4,
                'C': 5,
                'D': 10,
                'E': 20
            }
            return bet * payouts.get(symbol, 0)
        return 0

    def place_bet(self):
        """
        Prompt the user to place a bet and validate it.
        """
        while True:
            try:
                bet = int(input("Place your bet amount: "))
                if bet > self.balance:
                    print("Insufficient funds")
                elif bet <= 0:
                    print("Bet must be greater than 0")
                else:
                    return bet
            except ValueError:
                print("Please enter a valid number")

    def play_round(self):
        """
        Play a single round of the slot machine game.
        """
        bet = self.place_bet()
        self.balance -= bet

        row = self.spin_row()
        print("Spinning...\n")
        self.print_row(row)

        payout = self.get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry, you lost this round")

        self.balance += payout

    def start(self):
        """
        Start the slot machine game.
        """
        print("*************************")
        print("Welcome to Python Slots ")
        print("Symbols: A, B, C, D, E")
        print("*************************")

        while self.balance > 0:
            print(f"Current balance: ${self.balance}")
            self.play_round()

            play_again = input("Do you want to spin again? (Y/N): ").upper()
            if play_again != 'Y':
                break

        print("*******************************************")
        print(f"Game over! Your final balance is ${self.balance}")
        print("*******************************************")


if __name__ == '__main__':
    SlotMachine().start()
