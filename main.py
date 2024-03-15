class PortfolioManager:

    def __init__(self, initial_portfolio):
        self.catalogue = {initial_portfolio: {"stock": [], "amount": []}}
        self.balance = 10000

    def display_balance(self):
        """Displays the user's available balance"""
        print(f"Your available balance is: R{self.balance}")

    def new_portfolio(self):
        """Guides the user through the process of creating a new portfolio.
        This portfolio is then added to the catalogue dictionary."""
        new_port_name = input("Enter a name for your new portfolio: ").title()
        if new_port_name not in self.catalogue:
            self.catalogue[new_port_name] = {"stock": [], "amount": []}
            print(f"Portfolio: {new_port_name} created successfully!\n")
            input("\nPress enter to continue back to the menu.")
            return new_port_name
        else:
            print("This portfolio already exists! Choose a different name.")
            self.new_portfolio()

    def add_stock(self, portfolio):
        """Guides the user through the process of creating a new stock inside a given portfolio.
        An initial amount of this stock has to be brought and this stock is then added to the selected portfolio
        if funds are available."""

        stock_name = input("Enter the name of the stock you would like to add: ").title()
        if stock_name not in self.catalogue[portfolio]["stock"]:
            initial_shares = int(input("How much of this stock would you like to buy: R"))
            if self.balance - initial_shares >= 0:
                if portfolio in self.catalogue:
                    self.catalogue[portfolio]["stock"].append(stock_name)
                    self.catalogue[portfolio]["amount"].append(int(initial_shares))
                    self.balance -= initial_shares
                    print(f"R{initial_shares} of {stock_name} added to {portfolio}.\n")
                    return self.catalogue[portfolio]["stock"].index(stock_name)
                else:
                    print("This portfolio does not exist.\n")
                    return "error"
            else:
                print("Insufficient funds.\n")
                return "error"
        else:
            print("You already have this stock on your portfolio!\n")
            return "error"

    def buy_shares(self, portfolio, stock):
        """Guides the user through the process of buying shares of an existing stock within a given portfolio.
        If funds are available, this selected amount of stock is then purchased with the user's funds"""

        amount = int(input("Input the amount of shares you would like to buy: R"))
        if self.balance - amount >= 0:
            if portfolio in self.catalogue:
                stock_name = self.catalogue[portfolio]["stock"][stock]
                self.catalogue[portfolio]["amount"][stock] += amount
                self.balance -= amount
                print(f'R{amount} of {stock_name} bought successfully')
                self.display_balance()
                print("")
            else:
                print("This portfolio does not exist.")
        else:
            print("You have insufficient funds for this transaction. Display your balance to view your remaining "
                  "funds\n")

    def sell_shares(self, portfolio, stock):
        """Guides the user through the process of selling shares of an existing stock within a given portfolio.
        If the selected amount of stock is available, this selected amount of stock is then sold and added to
        the user's funds"""

        amount = int(input("Input the amount of shares you would like to sell: R"))
        if self.catalogue[portfolio]["amount"][stock] - amount >= 0:
            if portfolio in self.catalogue:
                stock_name = self.catalogue[portfolio]["stock"][stock]
                self.catalogue[portfolio]["amount"][stock] -= amount
                self.balance += amount
                print(f'R{amount} of {stock_name} sold successfully')
                self.display_balance()
            else:
                print("This portfolio does not exist.")
        else:
            print("You have insufficient shares for this transaction.\n")

    def deposit_money(self):
        """Guides the user through the process of adding funds to their account"""

        amount = int(input("Enter the amount you would like to deposit: R"))
        self.balance += amount
        print(f"R{amount} deposited successfully.")
        self.display_balance()

    def withdraw_money(self):
        """Guides the user through the process of withdrawing funds from their account"""

        self.display_balance()
        amount = int(input("Enter the amount you would like to withdraw: R"))
        if self.balance - amount >= 0:
            self.balance -= amount
            print(f"R{amount} withdrawn successfully.")
        else:
            print("Insufficient funds.")
        self.display_balance()

    def display_portfolios(self, display_stock_bool):
        """displays a list of the portfolios owned by the user in the portfolio's dictionary"""

        print("\nList of your Portfolios:")
        if display_stock_bool:
            for i in self.catalogue.keys():
                print(f"\n ----- {i} -----")
                j_num = 0
                for j in range(len(self.catalogue[i]["stock"])):
                    j_num += 1
                    print(f'{j_num} - {self.catalogue[i]["stock"][j-1]}: R{self.catalogue[i]["amount"][j-1]}')
        else:
            i_num = 0
            for i in self.catalogue.keys():
                i_num += 1
                print(f"{i_num} - {i}")

    def display_stock(self, portfolio, stock_index):
        """Displays a selected stock on a portfolio with the amount of owned stock"""

        stock_name = self.catalogue[portfolio]["stock"][stock_index]
        stock_amount = self.catalogue[portfolio]["amount"][stock_index]
        print(f"{stock_name} - R{stock_amount}")

    def display_specific_portfolio(self, portfolio):
        """Displays all the stocks and amounts on a selected portfolio"""

        print(f"\nHere are the stocks you have in {portfolio}:\n")
        for i in range(len(self.catalogue[portfolio]["stock"])):
            self.display_stock(portfolio, i)


on = True

print("Welcome to the portfolio manager Program.")
first_portfolio = input("To get started, Please enter the name of your first portfolio: ").title()
manager = PortfolioManager(first_portfolio)
print("\nHere is the portfolio manager menu. Enter a number for the corresponding command.")
print("Select or create a portfolio for to start buying or selling stocks! \n")


while on:

    portfolio_selected_bool = False
    stock_selected_bool = False

    print("1 - Create New Portfolio")
    print("2 - Select Portfolio")
    print("3 - Deposit Funds")
    print("4 - Withdraw Funds")
    print("5 - Display Balance")
    print("6 - Display Portfolios")
    print("/ - Exit Program")

    selection = input("Select an option to continue: ")
    print("")

    if selection == "1":
        selected_portfolio = manager.new_portfolio()
        portfolio_selected_bool = True
    elif selection == "2":
        manager.display_portfolios(False)
        selected_portfolio_key = int(input("\nEnter the number of the portfolio you would like to select: ")) - 1
        if selected_portfolio_key in range(len(manager.catalogue.keys())):
            keys = list(manager.catalogue.keys())
            selected_portfolio = keys[selected_portfolio_key]
            print(f"Portfolio {selected_portfolio} selected successfully.\n")
            portfolio_selected_bool = True
        else:
            print("The selected portfolio does not exist.")

    elif selection == "3":
        manager.deposit_money()
        input("\nPress enter to continue back to the menu.")
        print("")

    elif selection == "4":
        manager.withdraw_money()
        input("\nPress enter to continue back to the menu.")
        print("")

    elif selection == "5":
        manager.display_balance()
        input("\nPress enter to continue back to the menu.")
        print("")

    elif selection == "6":
        manager.display_portfolios(True)
        input("\nPress enter to continue back to the menu.")
        print("")

    elif selection == "/":
        on = False

    else:
        print("Invalid option. Please enter a number to continue.\n")

    while portfolio_selected_bool:
        stock_selected_bool = False

        print(f"--{selected_portfolio}--")
        print("1 - Add a Stock")
        print("2 - Select a Stock")
        print("3 - Portfolio Overview")
        print("0 - Back to Menu")
        selection = input("Please select one of the above options to continue:")
        print("")

        if selection == "1":
            selected_stock = (manager.add_stock(selected_portfolio))
            if selected_stock != "error":
                selected_stock = int(selected_stock)
                stock_selected_bool = True

        elif selection == "2":
            if len(manager.catalogue[selected_portfolio]["stock"]) > 0:
                for i in range(len(manager.catalogue[selected_portfolio]["stock"])):
                    print(f'{i + 1} - {manager.catalogue[selected_portfolio]["stock"][i]}')
                selected_stock = int(input("\nEnter the number of the stock you would like to select: ")) - 1
                stock_selected_bool = True
            else:
                print("You do not have any stocks on this portfolio!\n")

        elif selection == "3":
            print(f"\n--{selected_portfolio}--")
            for i in range(len(manager.catalogue[selected_portfolio]["stock"])):
                manager.display_stock(selected_portfolio, i)
            print("")

        elif selection == "0":
            portfolio_selected_bool = False
            print("")
            break
        else:
            print("Invalid selection")

        while stock_selected_bool:
            if selected_stock <= len(manager.catalogue[selected_portfolio]["stock"]):
                manager.display_stock(selected_portfolio, selected_stock)
                print("1 - Buy Shares")
                print("2 - Sell Shares")
                print("0 - Back to Portfolio")

                selection = input("Please select one of the above options to continue:")
                print("")

                if selection == "1":
                    manager.buy_shares(selected_portfolio, selected_stock)
                elif selection == "2":
                    manager.sell_shares(selected_portfolio, selected_stock)
                elif selection == "0":
                    stock_selected_bool = False
                    break
                else:
                    print("Invalid selection")
            else:
                print("Invalid stock selection")
