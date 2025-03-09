# Import time module to handle timestamps for blockchain transactions
import time
# Import sha256 from hashlib to generate cryptographic hashes for blocks
from hashlib import sha256


class Block:
 

    def __init__(self, index, previous_hash, transaction, timestamp=None):
        self.index = index  # Position of the block in the chain
        self.previous_hash = previous_hash  # Hash of the previous block to maintain integrity
        self.transaction = transaction  # Data stored in the block (e.g., transactions)
        self.timestamp = timestamp if timestamp else time.time()  # Time of block creation
        self.hash = self.calculate_hash()  # Unique hash of this block

    def calculate_hash(self):
        """Generates a SHA-256 hash for the block based on its contents."""
        return sha256(f"{self.index}{self.previous_hash}{self.transaction}{self.timestamp}".encode()).hexdigest()

class Blockchain:

    # Constructor initializes the blockchain with the genesis block
    def __init__(self):
        # Create the first block (genesis block) and add it to the blockchain
        self.chain = [self.create_genesis_block()]

    # Method to create the first block (genesis block) in the blockchain
    def create_genesis_block(self):
        # The genesis block has an index of 0.
        return Block(0, "0", "Genesis Block - Welcome")

    # Method to add a new block to the blockchain with a recorded transaction
    def add_block(self, transaction):
        # Get the last block in the chain to determine the previous hash
        previous_block = self.chain[-1]
        # Create a new block with the next index, previous block hash, and transaction data
        new_block = Block(len(self.chain), previous_block.hash, transaction)
        # Append the newly created block to the blockchain
        self.chain.append(new_block)

     # Method to print all blocks stored in the blockchain
    def view_chain(self):
        # Iterate through each block in the blockchain
        for block in self.chain:
            print(f"Index:{block.index}")
            print(f"Previous Hash:{block.previous_hash}")
            print(f"Transaction:{block.transaction}")
            print(f"Timestamp:{block.timestamp}")
            print(f"Hash:{block.hash}")
            print("-" * 50)

#Represents a user with a balance and owned shares in properties.
class User:
    def __init__(self, name, balance):
        self.name = name 
        self.balance = balance 
        self.owned_shares = {} 

    #Displays the user's current balance and owned shares in properties.
    def view_portfolio(self):
        print(f"User: {self.name}")
        print(f"Balance: {self.balance:.3f} REIT")
        print("Owned Shares:")
        for property, shares in self.owned_shares.items():
             # Loop through each property and display the number of shares owned
            print(f"  {property}: {shares} shares")

    #Allows a user to buy shares from a property if they have enough funds.
    def buy_shares(self, property, shares, blockchain):
        cost = sum(property.get_price(i) for i in range(property.remaining_shares - shares, property.remaining_shares))
         # Check if the user has enough balance to buy and if there are enough shares available
        if self.balance >= cost and property.remaining_shares >= shares:
            # Deduct the cost from the user's balance
            self.balance -= cost
             # Add the purchased shares to the user's owned shares
            self.owned_shares[property.name] = self.owned_shares.get(property.name, 0) + shares
            # Reduce the remaining shares of the property by the number of shares bought
            property.remaining_shares -= shares
            # Record the transaction in the blockchain
            blockchain.add_block(f"{self.name} bought {shares} shares of {property.name} for {cost:.3f} REIT")
            # Print a confirmation message showing transaction details and the new price per share
            print(f"{self.name} bought {shares} shares for {cost:.3f} REIT. The current price per share is now {property.get_price(property.remaining_shares):.3f} REIT. {property.remaining_shares} shares remaining.")
        else:
            print("Transaction failed: Insufficient balance or shares.")
    # Method to sell shares and receive payment based on the current share price
    def sell_shares(self, property, shares, blockchain):
        # Check if the user owns enough shares to sell
        if self.owned_shares.get(property.name, 0) >= shares:
             # Calculate the total amount earned 
            earned = sum(property.get_price(i) for i in range(property.remaining_shares, property.remaining_shares + shares))
            # Add the earned amount to the user's balance
            self.balance += earned
            # Deduct the sold shares from the user's owned shares
            self.owned_shares[property.name] -= shares
            # Increase the remaining shares of the property by the number of shares sold
            property.remaining_shares += shares
            # Record the transaction in the blockchain
            blockchain.add_block(f"{self.name} sold {shares} shares of {property.name} for {earned:.3f} REIT")
            # Print a confirmation message showing transaction details and the new price per share
            print(f"{self.name} sold {shares} shares for {earned:.3f} REIT. The current price per share is now {property.get_price(property.remaining_shares):.3f} REIT. {property.remaining_shares} shares remaining.")
        else:
            print("Transaction failed: Insufficient shares.")

# Represents a property available for investment with dynamically adjusting share prices.
class Property:
    def __init__(self, name, total_value):
        self.name = name  
        self.total_value = total_value  
        self.remaining_shares = 100000
        # Initial price per share (98% of full value) 
        self.P0 = (total_value / 100000) * 0.98 
        # Final price per share (102% of full value) 
        self.Pf = (total_value / 100000) * 1.02  

    # Calculates the price per share based on the number of remaining shares.
    def get_price(self, remaining_shares):
        return self.P0 + ((self.Pf - self.P0) * (100000 - remaining_shares) / 100000)

# Main function to run the interactive real estate blockchain application.
def main():
    blockchain = Blockchain()
    properties = {}
    users = {}
    
    while True:
        print("\nMenu:")
        print("1. Create New User")
        print("2. Create New Property Listing")
        print("3. Buy Shares")
        print("4. Sell Shares")
        print("5. View User Portfolio")
        print("6. View Blockchain")
        print("7. Exit")
        choice = input("Select an option: ")

         # Option to create a new user account
        if choice == "1":
            name = input("Enter user name: ")
            balance = float(input("Enter starting balance: "))
            users[name] = User(name, balance)
            # Print confirmation message for user creation
            print(f"User {name} created with {balance} REIT.")
	        # Add the new user event to the blockchain
            blockchain.add_block(f"New account created: {name} with {balance:.3f} REIT")
	    # Option to create a new property listing
        elif choice == "2":
            property_name = input("Enter property name or address: ")
            price = float(input("Enter total property price: "))
            properties[property_name] = Property(property_name, price)
            # Print confirmation message for property listing
            print(f"Property {property_name} listed with total price {price} REIT.")
            # Add the new property listing event to the blockchain
            blockchain.add_block(f"New property listed: {property_name} with total price {price:.3f} REIT")

	# Option to buy shares
        elif choice == "3":
            name = input("Enter your name: ")
            if name in users:
                property_name = input("Enter property name: ")
                if property_name in properties:
                    shares = int(input("Enter number of shares to buy: "))
                     # Execute the buy shares transaction and update the blockchain
                    users[name].buy_shares(properties[property_name], shares, blockchain)
                else:
                     # Display an error message if the property does not exist
                    print("Property not found. Create a listing first.")
            else:
                # Display an error message if the user does not exist
                print("User not found. Create a user first.")

	# Option to buy shares
        elif choice == "4":
            name = input("Enter your name: ")
            if name in users:
                property_name = input("Enter property name: ")
                if property_name in properties:
                    shares = int(input("Enter number of shares to sell: "))
                    # Execute the sell shares transaction and update the blockchain
                    users[name].sell_shares(properties[property_name], shares, blockchain)
                else:
                    # Display an error message if the property does not exist
                    print("Property not found.")
            else:
                # Display an error message if the user does not exist
                print("User not found. Create a user first.")
        
	# Option to view portfolio
        elif choice == "5":
             # Prompt user for the name of the user whose portfolio they want to view
            name = input("Enter user name to view portfolio: ")
            # Check if the user exists in the system
            if name in users:
                # Call the method to display the user's portfolio details
                users[name].view_portfolio()
            else:
                 # Display an error message if the user does not exist
                print("User not found.")
        
        # Display all recorded blocks in the blockchain
        elif choice == "6":
            blockchain.view_chain()
        
         # Option to exit the program
        elif choice == "7":
            # Print a message indicating the program is closing
            print("Exiting program.")
             # Terminate the loop and exit the application
            break

        else:
             # Display an error message for invalid input
            print("Invalid choice, please try again.")

# Entry point of the script, ensuring the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()
