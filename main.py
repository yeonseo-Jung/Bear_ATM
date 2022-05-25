import time

try: 
    import pandas as pd
except:
    import os
    os.system('pip install pandas')
    import pandas as pd
    
from atm import Account


def controller(card='', pin=''):
    while (len(card)!=6) | (card.isdigit()==False) & (len(pin)!=4) & (pin.isdigit()==False):
        print("\t===========")
        print("\tInsert Card")
        print("\t===========")
        card = input("Enter the Card Number (6 digit number): ")
        pin = input("Enter the PIN Number (4 digit number): ")
    
    ac = Account(card, pin)
    print("\n\t===========")
    print("\tINVALID PIN")
    print("\t===========")
    
    menu = -1
    while menu not in ['0', '1', '2', '3']:
        print('''
        =========================
        (0) View your balance
        (1) Deposit
        (2) Withdrawal
        (3) Transaction breakdown
        =========================
        ''')
        menu = input("Enter the Menu Number (Enter the '0' or '1' or '2' or '3'): ")
    
    if menu == '0':
        if len(ac.transaction) == 0:
            balance = "$ 0"
        else:
            balance = ac.transaction[-1][-1]
        print("\n\t====================")
        print(f'\tBalance: {balance}')
        print("\t====================")
        
    elif menu == '1':
        dollars = input("Enter the Amount to Deposit: ")
        while not dollars.isdigit():
            dollars = input("Enter the Amount to Deposit: ")
            
        ac.deposit(int(dollars))
        balance = ac.transaction[-1][-1]
        print("\n\t===============================")
        print(f'\tSuccessful Deposit of $ {dollars}')
        print("\t===============================")
        print(f'\tBalance: $ {balance}')
        print("\t===============================")
        
    elif menu == '2':
        dollars = input("Enter the Amount to Withdraw: ")
        while not dollars.isdigit():
            dollars = input("Enter the Amount to Withdraw: ")
            
        result, balance = ac.withdraw(int(dollars))
        while result == 0:      
            print('\n\t=====================================')     
            print(f'\tBalance: $ {balance}')
            print("\tI can't withdraw more than my balance")
            print('\t=====================================')
            dollars = input("Enter the Amount to Withdraw (If you don't want to withdraw, click 'n'): ")
            if dollars == "n" or dollars == "N":
                break
            else:
                result, balance = ac.withdraw(int(dollars))
        
        if result == 1:
            print("\n\t=====================================")
            print(f'\tSuccessful withdrawal of $ {dollars}')
            print("\t=====================================")
            print(f'\tBalance: $ {balance}')
            print("\t=====================================")
        
    elif menu == '3':
        if len(ac.transaction) == 0:
            print('\n\t==============')
            print("\tNo Transaction")
            print('\t==============')
        
        else:
            try:
                trans_df = pd.DataFrame(ac.transaction, columns=['Date', 'Deposit/Withdraw', 'Balance'])
                print("\n")
                print(trans_df)
            
            except:
                print("\n\t==================================================")
                print("\tDate\t\t    | Deposit/Withdraw   | Balance")
                print("\t==================================================")
                for trans in ac.transaction:
                    _trans = trans[1]
                    while len(_trans) < 18:
                        _trans = _trans + " "
                    
                    print(f'\t{trans[0]} | {_trans} | {trans[2]}')
                    print("\t==================================================")
    
    else:
        pass
    
    print("\n\t=============")        
    print("\tTake the card")
    print("\t=============")
    
if __name__ == '__main__':
    
    comp = "y"
    while comp == "y" or comp == "Y":
        controller()
        comp = input("\tDo you want to do another banking business? (Enter the 'y' or 'n')")
        
        while comp not in ['n', 'N', 'y', 'Y']:
            comp = input("\tDo you want to do another banking business? (Enter the 'y' or 'n')")
            
    print("\n\t========")
    print("\tGood Bye")
    print("\t========")
    time.sleep(2.5)