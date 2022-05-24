import os
import pickle
from datetime import datetime

root = os.path.dirname(os.path.realpath(__file__))
trans_cache_dir = os.path.join(root, 'trans_cache')

# Transaction cache directory
if not os.path.exists(trans_cache_dir):
    os.makedirs(trans_cache_dir)
    
class Account:
    def __init__(self, card, pin):
        self.card = card
        self.pin = pin
        self.account = f"Bear_{self.card}_{self.pin}.txt"
        self.account_path = os.path.join(trans_cache_dir, self.account)
        
        if os.path.isfile(self.account_path):
            with open(self.account_path, 'rb') as f:
                self.transaction = pickle.load(f)
        else:
            self.transaction = []

    def deposit(self, dollars):
        ''' Deposit function '''
        date = str(datetime.today())[0:19]
        
        # Balance check
        if len(self.transaction) == 0:
            balance = 0
        else:
            balance = int(self.transaction[-1][-1].replace('$ ', ''))
        
        # Deposit
        balance = balance + dollars
        self.transaction.append([date, f'+ $ {dollars}', f'$ {balance}'])
        
        # Save transaction 
        with open(self.account_path, 'wb') as f:
            pickle.dump(self.transaction, f)
        
    def withdraw(self, dollars):
        ''' Withdrawal function '''
        date = str(datetime.today())[0:19]
        
        # Balance check
        if len(self.transaction) == 0:
            balance = 0
        else:
            balance = int(self.transaction[-1][-1].replace('$ ', ''))
            
        # Withdraw
        if balance < dollars:   # lack of balance
            result = 0
        else:
            balance = balance - dollars
            self.transaction.append([date, f'- $ {dollars}', f'$ {balance}'])
            
            # Save transaction
            with open(self.account_path, 'wb') as f:
                pickle.dump(self.transaction, f)
            result = 1
            
        return result, balance 