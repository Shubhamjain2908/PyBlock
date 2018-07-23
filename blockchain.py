blockchain = [[1]]

def get_last_blockchain_value():
    return blockchain[-1]

def add_value(transaction_amount, last_transaction=get_last_blockchain_value()):
    blockchain.append([last_transaction, transaction_amount])

def get_user_input():
    return float(input('Your transaction amount please : '))

add_value(12, get_user_input())
add_value(last_transaction=get_last_blockchain_value(), transaction_amount =  23)
add_value(34, get_user_input())

print(blockchain)