def Init():
    newWallet = int(input('How much money do you have? '))
    return newWallet, []

def Add():
    global Wallet   # globalize local variable, so that Wallet can be modified
    newRecord = input('Add an expense or income record with description and amount: \n').split(', ')
    # print(f'record after split: {newRecord}')
    for index, data in enumerate(newRecord):
        # multi-assignment uses tuple defaultly
        newRecord[index] = data.split()[0], int(data.split()[1])
        Wallet += newRecord[index][1]
    # print(f'record after tuple: {newRecord}')
    return newRecord

def View(Wallet, Database):
    print("Here's your expense and income records: ")
    print("ITEM          AMOUNT")
    print("--------------------")
    for data in Database:
        print(f'{data[0]:<15s}{data[1]:>5d}')
    print("--------------------")
    print(f'Now you have {Wallet} dollars.')

def Delete():

def Exit():
    print('save file and exit')


Wallet, Database = Init()
while True:
    option = input('\nWhat do you want to do (add / view / delete / exit)? ')
    print('')
    if option == 'exit':
        Exit()
        break
    if option == 'add':
        # put list of tuples into Database
        Database.extend(Add())
    elif option == 'view':
        View(Wallet, Database)
    elif option == 'delete':
        break