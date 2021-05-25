import sys
# row format: 0-2 (num) 3-5 (|) 6-15 (category) 16-30 (description) 31-35 (amount)

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
                return newWallet, []
    else:   # read file if it exists
        retWallet, retRecord = 0, []
        for line in fh.readlines():
            try:
                if line[2].isdigit():   # find item No.
                    newCategory = ''.join([ch for i, ch in enumerate(line) if 6 <= i <= 15 and ch != ' '])   # find categorty of item and convert to str
                    newItem = ''.join([ch for i, ch in enumerate(line) if 16 <= i <= 30 and ch != ' '])   # find description of item and convert to str
                    newMoney = int(''.join([ch for i, ch in enumerate(line) if 31 <= i <= 35 and ch != ' ']))   # find amount of item and convert to int
                    retRecord.append((newCategory, newItem, newMoney))   # append as tuple
                elif line[:9] == 'Balance: ':   # find current wallent
                    retWallet = int(''.join([ch for i, ch in enumerate(line) if 9 <= i]))
            except Exception as errmsg:   # catch any kind of errors
                sys.stderr.write(f'Error: in ReadFile: {str(errmsg)}\n')
        print(f'Welcome back <3 You have {retWallet} dollars.')
        return retWallet, retRecord

def InitCategories():
    return ['expense', \
        ['food', ['meal', 'snack', 'drink'],\
        'transportation', ['bus', 'railway', 'MRT'],\
        'entertainment', ['movie', 'shop', 'game'],\
        'housing', ['medical', 'pet', 'bill']],\
        'income', ['salary', 'bonus']]

def Add(Records):
    global Wallet, Categories   # globalize local variable, so that variable can be modified
    while True:
        try:
            print('Add expense or income records:')
            newRecord = input('Format: <category> <description> <amount>, <category> <description> <amount>, ...\n').split(', ')

            # format normalization; split and multi-assign to a tuple
            for index, data in enumerate(newRecord):
                # [0] categoty, [1] description, [2] amount
                assert len(data.split()) == 3, "Multiple data should be separated by ', ' and no spaces in descripton."
                newRecord[index] = data.split()[0], data.split()[1], int(data.split()[2])
                assert len(data.split()[1]) < 16, 'Description should be less than 16 characters.'
                Wallet += newRecord[index][2]   # [2] amount
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
        if not Records:
            print('Nothing in your Accounting Book.')
        else:
            print("Here's your expense and income records.")
            print('No.   Category  Item          Amount')
            print('------------------------------------')
            for index, data in enumerate(Records, 1):
                print(f'{index:>3d} | {data[0]:<10s}{data[1]:<15s}{data[2]:>5d}')
            print('------------------------------------')
        print(f'You have {Wallet} dollars.')
    except Exception as errmsg:   # catch any kind of errors
        sys.stderr.write(f'Error: <View> {str(errmsg)}\n')

def Delete(Records):
    global Wallet
    if not Records:
        print('Nothing to delete.')
    else:
        print('No.   Category  Item          Amount')
        print('------------------------------------')
        for index, data in enumerate(Records, 1):
            print(f'{index:>3d} | {data[0]:<10s}{data[1]:<15s}{data[2]:>5d}')
        print('------------------------------------')
        while True:
            try:
                No = int(input('Enter No. you want to delete: '))
                assert 0 < No <= len(Records)
            except ValueError:
                sys.stderr.write(f'Error: Input should be an integer.\n')
            except AssertionError:   # out of range
                sys.stderr.write(f'Error: Input should be within 1 to {len(Records)}\n')
            else:   # uplate current datas
                Wallet -= Records[No - 1][2]   # [2] amount
                del Records[No - 1]
                View(Wallet, Records)
                return Records

def ViewCategories(data, level):
    # not string but str
    if type(data) == str:
        print(f"{'   ' * level}- {data}")
    else:
        for i in range(len(data)):
            ViewCategories(data[i], level + 1)

def Save(Wallet, Records):
    try:
        with open('AccountingBook.txt', 'w') as fh:
            if not Records:
                fh.write('Nothing in your Accounting Book.\n')
            else:
                fh.write('No.   Category  Item          Amount\n')
                fh.write('------------------------------------\n')
                for index, data in enumerate(Records, 1):
                    fh.write(f'{index:>3d} | {data[0]:<10s}{data[1]:<15s}{data[2]:>5d}')
                fh.write('------------------------------------\n')
            fh.write(f'Balance: {Wallet}\n')
    except OSError as errmsg:   # 11. 檔案出錯
        sys.stderr.write(f'Error: {str(errmsg)}\n')


Wallet, Records = Init()
Categories = InitCategories()

while True:
    try:
        command = input('What do you want to do (add / view / categories / delete / find / exit)? ')
        if command == 'exit':
            Save(Wallet, Records)
            print('GoodBye <3')
            break
        if command == 'add':
            Records = Add(Records)
        elif command == 'view':
            View(Wallet, Records)
        elif command == 'categories':
            ViewCategories(Categories, -1)
        elif command == 'delete':
            Records = Delete(Records)
        else:
            raise Exception('Invalid command.')
    except Exception as errmsg:
        sys.stderr.write(f'Error: {str(errmsg)}\n')