import sys
import string

def Init():
    try:
        fh = open('AccountingBook.txt', 'r')
        assert fh.readlines() != ''
        fh.seek(0)   # back to first line after using readlines()
    except (FileNotFoundError, AssertionError):   # create one if file doesn't exist or is empty
        print("Let's create an Accounting Book.")
        while True:
            try:
                newWallet = int(input('How much money do you have? '))
            except ValueError:
                sys.stderr.write('Error: Input should be an integer.\n')
            else:
                return newWallet, [], 0
    else:   # read file if it exists
        retWallet, retRecord, retCnt = 0, [], 0
        for line in fh.readlines():
            try:
                if line[2].isdigit():   # find item No.
                    newItem = ''.join([ch for i, ch in enumerate(line) if 6 <= i <= 20 and ch != ' '])   # find description of item and convert to str
                    newMoney = int(''.join([ch for i, ch in enumerate(line) if 21 <= i and ch != ' ']))   # find amount of item and convert to int
                    retRecord.append((newItem, newMoney))   # append as tuple
                    retCnt += 1
                elif line[:9] == 'Balance: ':   # find current wallent
                    retWallet = int(''.join([ch for i, ch in enumerate(line) if 9 <= i]))
            except Exception as errmsg:   # catch any kind of errors
                sys.stderr.write(f'Error: <ReadFile>: {str(errmsg)}\n')
        print(f'Welcome back <3 You have {retWallet} dollars.')
        return retWallet, retRecord, retCnt

def Add(Records):
    global Wallet, itemCnt   # globalize local variable, so that variable can be modified
    while True:
        try:
            print('Add expense or income records with descriptions and amounts:')
            newRecord = input('  <Format: item1 amount1, item2 amount2, ...>\n').split(', ')
            for index, data in enumerate(newRecord):
                # normalize the format of newRecord; split and multi-assign to a tuple
                assert len(data.split()) == 2, "Multiple data should be separated by ', ' and no spaces in descripton."
                newRecord[index] = data.split()[0], int(data.split()[1])
                assert len(data.split()[0]) < 16, 'Description should be less than 16 characters.'
                Wallet += newRecord[index][1]
                itemCnt += 1
        except AssertionError as errmsg:
            sys.stderr.write(f'Error: {str(errmsg)}\n')
        except ValueError:
            sys.stderr.write('Error: Money should be an integer.\n')
        else:
            Records.extend(newRecord)
            View(Wallet, Records)
            return Records

def View(Wallet, Records):
    try:
        global itemCnt
        if itemCnt == 0:
            print('Nothing in your Accounting Book.')
        else:
            print("Here's your expense and income records.")
            print('No.   Item          Amount')
            print('--------------------------')
            for index, data in enumerate(Records, 1):
                print(f'{index:>3d} | {data[0]:<15s}{data[1]:>5d}')
            print('--------------------------')
        print(f'You have {Wallet} dollars.')
    except Exception as errmsg:   # catch any kind of errors
        sys.stderr.write(f'Error: <View> {str(errmsg)}\n')

def Delete(Records):
    global Wallet, itemCnt
    if itemCnt == 0:
        print('Nothing to delete.')
    else:
        print('No.   Item          Amount')
        print('--------------------------')
        for index, data in enumerate(Records, 1):
            print(f'{index:>3d} | {data[0]:<15s}{data[1]:>5d}')
        print('--------------------------')
        while True:
            try:
                No = int(input('Enter No. you want to delete: '))
                assert 0 < No <= itemCnt
            except ValueError:
                sys.stderr.write(f'Error: Input should be an integer.\n')
            except AssertionError:   # out of range
                sys.stderr.write(f'Error: Input should be within 1 to {itemCnt}\n')
            else:   # uplate current datas
                Wallet -= Records[No - 1][1]
                itemCnt -= 1
                del Records[No - 1]
                View(Wallet, Records)
                return Records

def Save(Wallet, Records, itemCnt):
    try:
        with open('AccountingBook.txt', 'w') as fh:
            if itemCnt == 0:
                fh.write('Nothing in your Accounting Book.\n')
            else:
                fh.write('No.   Item          Amount\n')
                fh.write('--------------------------\n')
                for index, data in enumerate(Records, 1):
                    fh.write(f'{index:>3d} | {data[0]:<15s}{data[1]:>5d}\n')
                fh.write('--------------------------\n')
            fh.write(f'Balance: {Wallet}\n')
    except OSError as errmsg:   # 11. 檔案出錯
        sys.stderr.write(f'Error: {str(errmsg)}\n')


Wallet, Records, itemCnt = Init()
while True:
    try:
        option = input('\nWhat do you want to do (add / view / delete / exit)? ')
        if option == 'exit':
            Save(Wallet, Records, itemCnt)
            print('GoodBye <3')
            break
        if option == 'add':
            Records = Add(Records)
        elif option == 'view':
            View(Wallet, Records)
        elif option == 'delete':
            Records = Delete(Records)
        else:
            raise Exception('Invalid command.')
    except Exception as errmsg:
        sys.stderr.write(f'Error: {str(errmsg)}\n')