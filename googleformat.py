UNOCCUPIED_TABLES = [ 1, 2, 3, 4, 5]
OCCUPIED_TABLES = []
global CURRENT_TABLE
global MANAGER_INVENTORY
MANAGER_INVENTORY = TableOrder()

class TableOrder():
    def __init__(self):
        self.appetizer = 0
        self.vegetarian = 0
        self.entree = 0
        self.dessert = 0
        self.payment = 0

def check_open():
    if not UNOCCUPIED_TABLES:
        print 'No open tables!'
    if UNOCCUPIED_TABLES:
        for table in UNOCCUPIED_TABLES:
            print table, 'Table'
        print '-' * 10

def show_taken():
    if not OCCUPIED_TABLES:
        return False

def show_tables():
    global CURRENT_TABLE
    global TABLE1
    global TABLE2
    global TABLE3
    global TABLE4
    global TABLE5
    check_open()
    display_loop = True
    if display_loop:
        table_selection = input('Select a table:')
        if int(table_selection) in OCCUPIED_TABLES:
            display_loop = True
        if int(table_selection) in UNOCCUPIED_TABLES:
            UNOCCUPIED_TABLES.remove(int(table_selection))
            OCCUPIED_TABLES.append(int(table_selection))
            "table"+table_selection = Order()
            CURRENT_TABLE = "table" + table_selection
            display_loop = False
        table_order()

def table_order():
    print 'A Add Items'
    print 'R Remove Items'
    print 'D Done'
    print '-' * 15
    action_loop = True
    while action_loop:
        user_choice = input('Enter a choice:')
        if user_choice.upper() == 'A':
            action_loop = False
            add_tem()
        if user_choice.upper() == 'R':
            action_loop = False
            remove_item()
        if user_choice.upper() == 'D':
            action_loop = False

def add_item():
    global CURRENT_TABLE
    choices_arr = [ 1, 2, 3, 4]
    menu_loop = True
    show_menu()
    if menu_loop:
        add_food = input('Enter a choice:')
        if int(add_food) == 1;
            valid_loop == True
            if valid_loop;
                app_quant = input('Total appetizers:')
                if app_quant.isdigit() == True:
                    valid_loop = False
                    currentapp = CURRENT_TABLE.appetizer
                    CURRENT_TABLE.appetizer = currentapp + app_quant
                    menu_loop = True
                    valid_loop = False
                if app_quant.isdigit() == False:
                    print('Invalid. Please enter an integer. ')
                    valid_loop = True:
        if int(add_food) == 2;
            valid_loop == True
            if valid_loop;
                veg_quant = input('Total vegetarian:')
                if veg_quant.isdigit() == True:
                    valid_loop = False
                    currentveg = CURRENT_TABLE.vegetarian
                    CURRENT_TABLE.vegetarian = currentveg + veg_quant
                    menu_loop = True
                    valid_loop = False
                if veg_quant.isdigit() == False:
                    print('Invalid. Please enter an integer. ')
                    valid_loop = True:
        if int(add_food) == 3;
            valid_loop == True
            if valid_loop;
                entree_quant = input('Total entrees:')
                if entree_quant.isdigit() == True:
                    valid_loop = False
                    currententree = CURRENT_TABLE.entree
                    CURRENT_TABLE.entree = currententree + entree_quant
                    menu_loop = True
                    valid_loop = False
                if entree_quant.isdigit() == False:
                    print('Invalid. Please enter an integer. ')
                    valid_loop = True:
        if int(add_food) == 4;
            valid_loop == True
            if valid_loop;
                des_quant = input('Total dessert:')
                if des_quant.isdigit() == True:
                    valid_loop = False
                    currentdes = CURRENT_TABLE.dessert
                    CURRENT_TABLE.dessert = currentdes + des_quant
                    menu_loop = True
                    valid_loop = False
                if des_quant.isdigit() == False:
                    print('Invalid. Please enter an integer. ')
                    valid_loop = True:
        if add_food == 'D':
            menu_loop = False

def remove_item():
    global CURRENT_TABLE
    tableitems = []
    itemnumer = []

    if CURRENT_TABLE.appetizer != 0:
        tableitems.append('1 Appetizer %s' % CURRENT_TABLE.appetizer)
        itemnumber.append(1)
    if CURRENT_TABLE.vegetar != 0:
        tableitems.append('2 Vegetarian %s' % CURRENT_TABLE.vegetarian)
        itemnumber.append(2)
    if CURRENT_TABLE.entree != 0:
        tableitems.append('3 Entree %s' % CURRENT_TABLE.entree)
        itemnumber.append(3)
    if CURRENT_TABLE.dessert != 0:
        tableitems.append('4 Dessert 1 %s' % CURRENT_TABLE.dessert)
        itemnumber.append(4)
    if not tableitems:
        print('No items to remove.')
        table_order()
    else:
        firstloop = 0
        while firstloop == 0:
            for tableitem in tableitems:
                print(tableitem)
            print('D Done')
            print('------------')
            deleteChoice = input('Enter Choice > ')
            if deleteChoice.upper() == 'D':
                firstloop = 1
                Table_Order()
            elif int(deleteChoice) in itemnumber:
                firstloop = 1
                delete_item_assignment(int(deleteChoice))
            else:
                firstloop = 0

def delete_item_assignment(deleteChoice):
    global CURRENT_TABLE
    if deleteChoice == 1:
        choiceAmount = CURRENT_TABLE.appetizer
        foodName = 'Appetizers'
        delete_item(foodName, choiceAmount, deleteChoice)
    elif deleteChoice == 2:
        choiceAmount = CURRENT_TABLE.salad
        foodName = 'Vegetarian'
        delete_item(foodName, choiceAmount, deleteChoice)
    elif deleteChoice == 3:
        choiceAmount = CURRENT_TABLE.soup
        foodName = 'Entree'
       delete_item(foodName, choiceAmount, deleteChoice)
    elif deleteChoice == 4:
        choiceAmount = CURRENT_TABLE.entree1
        foodName = 'Dessert'
        delete_item(foodName, choiceAmount, deleteChoice)

def delete_item(foodName, choiceAmount, deleteChoice):
    global CURRENT_TABLE
    choiceLoop = 0

    while choiceLoop == 0:
        deleteInput = input('Remove how many %s [0 - %s]> ' % (foodName, choiceAmount))
        if int(deleteInput) < 0:
            print('Invalid must be at least 0.')
            choiceLoop = 0
        elif int(deleteInput) > choiceAmount:
            print('Invalid must be most %s' % choiceAmount)
            choiceLoop = 0
        else:
            if deleteChoice == 1:
                CURRENT_TABLE.appetizer = choiceAmount - int(deleteInput)
                choiceLoop = 666
                Remove_Item()
            elif deleteChoice == 2:
                CURRENT_TABLE.vegetarian = choiceAmount - int(deleteInput)
                choiceLoop = 666
                Remove_Item()
            elif deleteChoice == 3:
                CURRENT_TABLE.entree = choiceAmount - int(deleteInput)
                choiceLoop = 666
                Remove_Item()
            elif deleteChoice == 4:
                CURRENT_TABLE.dessert = choiceAmount - int(deleteInput)
                choiceLoop = 666
                Remove_Item()

def print_bill():
    show_taken()
    if  show_taken() == False:
        print('No orders started yet!')
        return False
    else:
        for number in  sorted(Occupied):
            print(number, 'Table', number)
        print('-' * 9)
    billLoop = 0
    while billLoop == 0:
        billTable = input('Select a Table > ')
        for number in Occupied:
            if number == billTable:
                billLoop = 1
                select_table(billTable)
            else:
                billLoop = 7

def select_table(table_num):
    global TABLEID
    global CURRENT_TABLE
    if int(table_num) == 1:
        CURRENT_TABLE = table1
        TABLEID = "1"
    elif int(table_num) == 2:
        CURRENT_TABLE = table2
        TABLEID = "2"
    elif int(table_num) == 3:
        CURRENT_TABLE = table3
        TABLEID = "3"
    elif int(table_num) == 4:
        CURRENT_TABLE = table4
        TABLEID = "4"
    elif int(table_num) == 5:
        CURRENT_TABLE = table5
        TABLEID = "5"
    show_bill(TABLEID)



def show_menu():
    print '1 Appetizer'
    print '2 Vegetarian'
    print '3 Entree'
    print '4 Dessert'
    print 'D Done'
    print '-' * 15

def main():
    terminate = False
    loop = true
    init_choices = {
        'S': 'Start New Order',
        'E': 'Edit Order',
        'P': 'Print Bill',
        'R': 'Receive Payment',
        'M': 'Manager Report',
        'Q': 'Quit',
    }
    while not terminate:
        print('\n')
        for init_letter, init_value in init_choices:
            print(init_letter, init_choices)
        print '-' * 10
        user_choice = ' '
        while user_choice not in init_choices.keys():
            user_choice = input ("Enter Choice: ")
            user_choice = user_choice.strip().upper()
            if not user_choice:
                user_choice = ' '
            if userChoice == 'S':
                show_tables()
            if choice == 'E':
                edit_order()
            if choice == 'P':
                print_bill()
            if choice == 'R':
                receive_payment()
            if choice == 'M':
                show_report()
            if choice == 'Q':
                terminate = True

if __name__ == '__main__':
    main()
