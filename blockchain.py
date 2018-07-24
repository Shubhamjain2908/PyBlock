#Initializing our blockchain list
blockchain = [[1]]

def get_last_blockchain_value():
    """ Returns the last value of the blockchain. """
    return blockchain[-1]

def add_value(transaction_amount, last_transaction=get_last_blockchain_value()):
    """ Append a new value as well as the last blockchain value to the blockchain.
    
    Arguments:
        :transaction_amount: The amount that should be added
        :last_transaction: The last blockchain transaction (default [1]).
    """
    
    blockchain.append([last_transaction, transaction_amount])

def get_user_input():
    """ Returns the input of the user (a new transaction amount) as a float. """
    return float(input('Your transaction amount please : '))

add_value(12, get_user_input())
add_value(last_transaction=get_last_blockchain_value(), transaction_amount =  23)
add_value(34, get_user_input())

print(blockchain)