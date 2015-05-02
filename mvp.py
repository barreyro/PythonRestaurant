Unoccupied = ['1', '2', '3', '4', '5']
Occupied = []

class Order():
    def __init__(self):
        self.appetizer = 0
        self.salad = 0
        self.soup = 0
        self.entree1 = 0
        self.entree2 = 0
        self.dessert = 0
        self.payment = 0

global ManInventory
ManInventory = Order()

def Check_Open():
    if Unoccupied == []:
        print('No available tables at this time!')
    else:
        for number in Unoccupied:
            print(number, 'Table', number)
        print('-' * 9)

def Show_Taken():
    if Occupied == []:
        return False

def Show_Tables():
    global CurrentTable
    global table1
    global table2
    global table3
    global table4
    global table5
    Check_Open()
    i = 0
    while i == 0:
        TableChoice = input('Select a table> ')
        if TableChoice in Occupied:
            i = 0
        else:
            if TableChoice == '1':
                Unoccupied.remove('1')
                Occupied.append('1')
                table1 = Order()
                CurrentTable = table1
                i = 1
            if TableChoice == '2':
                Unoccupied.remove('2')
                Occupied.append('2')
                table2 = Order()
                CurrentTable = table2
                i = 1
            if TableChoice == '3':
                Unoccupied.remove('3')
                Occupied.append('3')
                table3 = Order()
                CurrentTable = table3
                i = 1
            if TableChoice == '4':
                Unoccupied.remove('4')
                Occupied.append('4')
                table4 = Order()
                CurrentTable = table4
                i = 1
            if TableChoice == '5':
                Unoccupied.remove('5')
                Occupied.append('5')
                table5 = Order()
                CurrentTable = table5
                i = 1
        Table_Order()

def Edit_Order():
    global CurrentTable
    Show_Taken()
    if Show_Taken() == False:
        print('No orders started yet!')
        return False
    else:
        for number in sorted(Occupied):
            print(number, 'Table', number)
        print('-' * 9)
        i = 0
        while i == 0:
            tableNumber = input('Select a table> ')
            if tableNumber in Occupied:
                i = 1
                if tableNumber == "1":
                    CurrentTable = table1
                elif tableNumber == "2":
                    CurrentTable = table2
                elif tableNumber == "3":
                    CurrentTable = table3
                elif tableNumber == "4":
                    CurrentTable = table4
                elif tableNumber == "5":
                    CurrentTable = table5
                Table_Order()
            else:
                i = 0

def Table_Order():
    print('A Add Items')
    print('R Remove Items')
    print('D Done')
    print('-' * 14)
    i = 0
    while i == 0:
        Choice = input('Enter Choice> ')
        if Choice.upper() == 'A':
            i = 1
            Add_Item()
        elif Choice.upper() == 'R':
            i = 1
            Remove_Item()
        elif Choice.upper() == 'D':
            i = 1
        else:
            i = 0

def Add_Item():
    global CurrentTable
    i = 0
    while i == 0:
        print('1 Appetizer')
        print('2 Salad')
        print('3 Soup')
        print('4 Entree 1')
        print('5 Entree 2')
        print('6 Dessert')
        print('D Done')
        print('-----------')
        AddChoice = input('Enter Choice> ')
        if AddChoice == '1':
            j = 0
            while j == 0:
                quantity = input('Add how many Appetizers> ')
                if quantity.isdigit() == True:
                    intvar = int(float(quantity))
                    currentappetizer = CurrentTable.appetizer
                    CurrentTable.appetizer = currentappetizer + intvar
                    j = 1
                    i = 0
                else:
                    print('Invalid must be at least 0.')
                    j = 0
        elif AddChoice == '2':
            j = 0
            while j == 0 :
                quantity = input('Add how many Salads> ')
                if quantity.isdigit() == True:
                    intvar = int(float(quantity))
                    currentsalad = CurrentTable.salad
                    CurrentTable.salad = currentsalad + intvar
                    j = 1
                    i = 0
                else:
                    print('Invalid must be at least 0.')
                    j = 0
        elif AddChoice == '3':
            j = 0
            while j == 0:
                quantity = input('Add how many Soups> ')
                if quantity.isdigit() == True:
                    intvar = int(float(quantity))
                    currentsoup = CurrentTable.soup
                    CurrentTable.soup = currentsoup + intvar
                    j = 1
                    i = 0
                else:
                    print('Invalid must be at least 0.')
                    j = 0
        elif AddChoice == '4':
            j = 0
            while j == 0:
                quantity = input('Add how many Entree 1> ')
                if quantity.isdigit() == True:
                    intvar = int(float(quantity))
                    currententree1 = CurrentTable.entree1
                    CurrentTable.entree1 = currententree1 + intvar
                    j = 1
                    i = 0
                else:
                    print('Invalid must be at least 0.')
                    j = 0
        elif AddChoice == '5':
            j = 0
            while j == 0:
                quantity = input('Add how many Entree 2> ')
                if quantity.isdigit() == True:
                    intvar = int(float(quantity))
                    currententree2 = CurrentTable.entree2
                    CurrentTable.entree2 = currententree2 + intvar
                    j = 1
                    i = 0
                else:
                    print('Invalid must be at least 0.')
                    j = 0
        elif AddChoice == '6':
            j = 0
            while j == 0:
                quantity = input('Add how many Desserts> ')
                if quantity.isdigit() == True:
                    intvar = int(float(quantity))
                    currentdessert = CurrentTable.dessert
                    CurrentTable.dessert = currentdessert + intvar
                    j = 1
                    i = 0
                else:
                    print('Invalid must be at least 0.')
                    j = 0
        elif AddChoice.upper() == 'D':
            i = 69
        else:
            i = 0

def Remove_Item():
    global CurrentTable
    tableitems = []
    itemnumber = []

    if CurrentTable.appetizer != 0:
        tableitems.append('1 Appetizer %s' % CurrentTable.appetizer)
        itemnumber.append(1)
    if CurrentTable.salad != 0:
        tableitems.append('2 Salad %s' % CurrentTable.salad)
        itemnumber.append(2)
    if CurrentTable.soup != 0:
        tableitems.append('3 Soup %s' % CurrentTable.soup)
        itemnumber.append(3)
    if CurrentTable.entree1 != 0:
        tableitems.append('4 Entree 1 %s' % CurrentTable.entree1)
        itemnumber.append(4)
    if CurrentTable.entree2 != 0:
        tableitems.append('5 Entree 2 %s' % CurrentTable.entree2)
        itemnumber.append(5)
    if CurrentTable.dessert != 0:
        tableitems.append('6 Dessert %s' % CurrentTable.dessert)
        itemnumber.append(6)
    if not tableitems:
        print('No items to remove.')
        Table_Order()
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
                Delete_Item_Assignment(int(deleteChoice))
            else:
                firstloop = 0

def Delete_Item_Assignment(deleteChoice):
    global CurrentTable
    if deleteChoice == 1:
        choiceAmount = CurrentTable.appetizer
        foodName = 'Appetizers'
        Delete_Item(foodName, choiceAmount, deleteChoice)
    elif deleteChoice == 2:
        choiceAmount = CurrentTable.salad
        foodName = 'Salads'
        Delete_Item(foodName, choiceAmount, deleteChoice)
    elif deleteChoice == 3:
        choiceAmount = CurrentTable.soup
        foodName = 'Soups'
        Delete_Item(foodName, choiceAmount, deleteChoice)
    elif deleteChoice == 4:
        choiceAmount = CurrentTable.entree1
        foodName = 'Entree 1s'
        Delete_Item(foodName, choiceAmount, deleteChoice)
    elif deleteChoice == 5:
        choiceAmount = CurrentTable.entree2
        foodName = 'Entree 2s'
        Delete_Item(foodName, choiceAmount, deleteChoice)
    elif deleteChoice == 6:
        choiceAmount = CurrentTable.dessert
        foodName = 'Desserts'
        Delete_Item(foodName, int(choiceAmount), int(deleteChoice))

def Delete_Item(foodName, choiceAmount, deleteChoice):
    global CurrentTable
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
                CurrentTable.appetizer = choiceAmount - int(deleteInput)
                choiceLoop = 666
                Remove_Item()
            elif deleteChoice == 2:
                CurrentTable.salad = choiceAmount - int(deleteInput)
                choiceLoop = 666
                Remove_Item()
            elif deleteChoice == 3:
                CurrentTable.soup = choiceAmount - int(deleteInput)
                choiceLoop = 666
                Remove_Item()
            elif deleteChoice == 4:
                CurrentTable.entree1 = choiceAmount - int(deleteInput)
                choiceLoop = 666
                Remove_Item()
            elif deleteChoice == 5:
                CurrentTable.entree2 = choiceAmount - int(deleteInput)
                choiceLoop = 666
                Remove_Item()
            elif deleteChoice == 6:
                CurrentTable.dessert = choiceAmount - int(deleteInput)
                choiceLoop = 666
                Remove_Item()

def Print_Bill():
    Show_Taken()
    if Show_Taken() == False:
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
                Select_Table(billTable)
            else:
                billLoop = 7

def Select_Table(tableNumber):
    global tableID
    global CurrentTable
    if int(tableNumber) == 1:
        CurrentTable = table1
        tableID = "1"
    elif int(tableNumber) == 2:
        CurrentTable = table2
        tableID = "2"
    elif int(tableNumber) == 3:
        CurrentTable = table3
        tableID = "3"
    elif int(tableNumber) == 4:
        CurrentTable = table4
        tableID = "4"
    elif int(tableNumber) == 5:
        CurrentTable = table5
        tableID = "5"
    Show_Bill(tableID)

def Show_Bill(tableID):
    global CurrentTable
    showLoop = 0
    while showLoop == 0:
        billList = []
        count = 0
        appTotal = CurrentTable.appetizer * 5.00
        saladTotal = CurrentTable.salad * 3.00
        soupTotal = CurrentTable.soup * 3.50
        entree1Total = CurrentTable.entree1 * 10.00
        entree2Total = CurrentTable.entree2 * 12.50
        dessertTotal = CurrentTable.dessert * 4.25
        subtotal = appTotal + saladTotal + soupTotal + entree2Total + entree1Total + dessertTotal
        tax8 = subtotal * .08
        totaltotal = subtotal + tax8
        tip10 = subtotal * .10
        tip15 = subtotal *.15
        tip20 = subtotal *.20

        CurrentTable.payment = totaltotal

        print('Bill for Table %s' % tableID)
        print('-' * 36)

        if CurrentTable.appetizer != 0:
            count = count + 1
            print('1. Appetizer ', appSpace(CurrentTable.appetizer), '@ $ 5.00: $%7s' % (("{0:.2f}".format(appTotal))))
        if CurrentTable.salad !=0:
            count = count + 1
            newcount = str(count)
            saladString = str(("{0:.2f}".format(saladTotal)))
            print('%s. Salad     ' % (newcount), appSpace(CurrentTable.salad), '@ $ 3.00: $%7s' % (saladString))
        if CurrentTable.soup !=0:
            count = count + 1
            newcount = str(count)
            soupString = str(("{0:.2f}".format(soupTotal)))
            print('%s. Soup      ' % (newcount), appSpace(CurrentTable.soup), '@ $ 3.50: $%7s' % (soupString))
        if CurrentTable.entree1 !=0:
            count = count + 1
            newcount = str(count)
            entree1String = str(("{0:.2f}".format(entree1Total)))
            print('%s. Entree1   ' % (newcount), appSpace(CurrentTable.entree1), '@ $10.00: $%7s' % (entree1String))
        if CurrentTable.entree2 !=0:
            count = count + 1
            newcount = str(count)
            entree2String = str(("{0:.2f}".format(entree2Total)))
            print('%s. Entree2   ' % (newcount), appSpace(CurrentTable.entree2), '@ $12.50: $%7s' % (entree2String))
        if CurrentTable.dessert !=0:
            count = count + 1
            newcount = str(count)
            dessertString = str(("{0:.2f}".format(dessertTotal)))
            print('%s. Dessert   ' % (newcount), appSpace(CurrentTable.dessert), '@ $ 4.25: $%7s' % (dessertString))
        if CurrentTable.dessert == 0 and CurrentTable.entree1 == 0 and CurrentTable.entree2 == 0 and CurrentTable.salad == 0 and CurrentTable.soup == 0 and CurrentTable.appetizer == 0:
            print('No Items Purchased        : $   0.00')

        print('                          :         ')
        print('Subtotal                  : $%7s' % (("{0:.2f}".format(subtotal))))
        print('Tax 8%%                    : $%7s' % (("{0:.2f}".format(tax8))))
        print('Total                     : $%7s' % (("{0:.2f}".format(totaltotal))))
        print('-' * 36)
        print('Suggested Tip')
        print('Tip 10%%                   : $%7s' % (("{0:.2f}".format(tip10))))
        print('Tip 15%%                   : $%7s' % (("{0:.2f}".format(tip15))))
        print('Tip 20%%                   : $%7s' % (("{0:.2f}".format(tip20))))
        print('-' * 36)
        showLoop = 1

def appSpace(appInt):
    if appInt == 1:
        return("   ")
    elif len(str(appInt)) > 1:
        return("x%2i" % (appInt))
    elif appInt < 10:
        return("x %1i" % (appInt))

def showCount(number):
    if (len(str(number))) == 3:
        return("x%s" % (str(number)))
    elif (len(str(number))) == 2:
        return("x %s" % (str(number)))
    elif (len(str(number))) == 1:
        return("    ")
    else:
        return("x", number)

def Receive_Payment():
    global CurrentTable
    Show_Taken()
    if Show_Taken() == False:
        print('No orders started yet!')
        return False
    else:
        for number in  sorted(Occupied):
            print(number, 'Table', number)
        print('-' * 9)
    i = 0
    while i == 0:
        tableNumber = input('Select a table> ')
        if tableNumber in Occupied:
            i = 1
            if int(tableNumber) == 1:
                CurrentTable = table1
            elif int(tableNumber) == 2:
                CurrentTable = table2
            elif int(tableNumber) == 3:
                CurrentTable = table3
            elif int(tableNumber) == 4:
                CurrentTable = table4
            elif int(tableNumber) == 5:
                CurrentTable = table5
            Print_Receipt(tableNumber)
        else:
            i = 0

def Print_Receipt(tableNumber):
    global ManInventory
    count = 0
    appTotal = CurrentTable.appetizer * 5.00
    saladTotal = CurrentTable.salad * 3.00
    soupTotal = CurrentTable.soup * 3.50
    entree1Total = CurrentTable.entree1 * 10.00
    entree2Total = CurrentTable.entree2 * 12.50
    dessertTotal = CurrentTable.dessert * 4.25
    subtotal = appTotal + saladTotal + soupTotal + entree2Total + entree1Total + dessertTotal
    tax8 = subtotal * .08
    totaltotal = subtotal + tax8
    tip10 = subtotal * .10
    tip15 = subtotal *.15
    tip20 = subtotal *.20
    paymentLoop = 0
    while paymentLoop == 0:
        paymentString = input('Enter payment for Table %s> ' % (tableNumber))
        paymentFloat = float(paymentString)
        if paymentFloat < totaltotal:
            print('Invalid must be at least %s' % (totaltotal))
            paymentLoop = 0
        else:
            count = 1
            changeFloat = totaltotal - paymentFloat
            print('Bill for Table %s' % tableNumber)
            print('-' * 36)

            if CurrentTable.appetizer !=0:
                count = count + 1
                print('1. Appetizer ', appSpace(CurrentTable.appetizer), '@ $ 5.00: $%7s' % (("{0:.2f}".format(appTotal))))
            if CurrentTable.salad !=0:
                count = count + 1
                newcount = str(count)
                saladString = str(("{0:.2f}".format(saladTotal)))
                print('%s. Salad     ' % (newcount), appSpace(CurrentTable.salad), '@ $ 3.00: $%7s' % (saladString))
            if CurrentTable.soup !=0:
                count = count + 1
                newcount = str(count)
                soupString = str(("{0:.2f}".format(soupTotal)))
                print('%s. Soup      ' % (newcount), appSpace(CurrentTable.soup), '@ $ 3.50: $%7s' % (soupString))
            if CurrentTable.entree1 !=0:
                count = count + 1
                newcount = str(count)
                entree1String = str(("{0:.2f}".format(entree1Total)))
                print('%s. Entree1   ' % (newcount), appSpace(CurrentTable.entree1), '@ $10.00: $%7s' % (entree1String))
            if CurrentTable.entree2 !=0:
                count = count + 1
                newcount = str(count)
                entree2String = str(("{0:.2f}".format(entree2Total)))
                print('%s. Entree2   ' % (newcount), appSpace(CurrentTable.entree2), '@ $12.50: $%7s' % (entree2String))
            if CurrentTable.dessert !=0:
                count = count + 1
                newcount = str(count)
                dessertString = str(("{0:.2f}".format(dessertTotal)))
                print('%s. Dessert   ' % (newcount), appSpace(CurrentTable.dessert), '@ $ 4.25: $%7s' % (dessertString))
            if CurrentTable.dessert == 0 and CurrentTable.entree1 == 0 and CurrentTable.entree2 == 0 and CurrentTable.salad == 0 and CurrentTable.soup == 0 and CurrentTable.appetizer == 0:
                print('No Items Purchased        : $   0.00')

            print('                          :         ')
            print('Subtotal                  : $%7s' % (("{0:.2f}".format(subtotal))))
            print('Tax 8%%                    : $%7s' % (("{0:.2f}".format(tax8))))
            print('Total                     : $%7s' % (("{0:.2f}".format(totaltotal))))
            print('-' * 36)
            print('Payment                   : $%7s' % (("{0:.2f}".format(paymentFloat))))
            print('Change                    : $%7s' % (("{0:.2f}".format(changeFloat))))
            print('-' * 36)

            Add_ManInv(CurrentTable.dessert, CurrentTable.entree1, CurrentTable.entree2, CurrentTable.salad, CurrentTable.soup, CurrentTable.appetizer)
            paymentLoop = 1

def Add_ManInv(dessert, entree1, entree2, salad, soup, appetizer):
    global ManInventory
    ManInventory.dessert = ManInventory.dessert + int(dessert)
    ManInventory.entree1 = ManInventory.entree1 + int(entree1)
    ManInventory.entree2 = ManInventory.entree2 + int(entree2)
    ManInventory.soup = ManInventory.soup + int(soup)
    ManInventory.salad = ManInventory.salad + int(salad)
    ManInventory.appetizer = ManInventory.appetizer + int(appetizer)

def Show_ManReport():
    showLoop = 0
    while showLoop ==0:
        pass
        count = 0
        appTotal = ManInventory.appetizer * 5.00
        saladTotal = ManInventory.salad * 3.00
        soupTotal = ManInventory.soup * 3.50
        entree1Total = ManInventory.entree1 * 10.00
        entree2Total = ManInventory.entree2 * 12.50
        dessertTotal = ManInventory.dessert * 4.25
        subtotal = appTotal + saladTotal + soupTotal + entree2Total + entree1Total + dessertTotal
        tax8 = subtotal * .08
        totaltotal = subtotal + tax8

        ManInventory.payment = totaltotal

        print('Daily Totals')
        print('-' * 36)

        if ManInventory.appetizer != 0:
            count = count + 1
            print('1. Appetizer ', appSpace(ManInventory.appetizer), '@ $ 5.00: $%7s' % (("{0:.2f}".format(appTotal))))
        if ManInventory.salad !=0:
            count = count + 1
            newcount = str(count)
            saladString = str(("{0:.2f}".format(saladTotal)))
            print('%s. Salad     ' % (newcount), appSpace(ManInventory.salad), '@ $ 3.00: $%7s' % (saladString))
        if ManInventory.soup !=0:
            count = count + 1
            newcount = str(count)
            soupString = str(("{0:.2f}".format(soupTotal)))
            print('%s. Soup      ' % (newcount), appSpace(ManInventory.soup), '@ $ 3.50: $%7s' % (soupString))
        if ManInventory.entree1 !=0:
            count = count + 1
            newcount = str(count)
            entree1String = str(("{0:.2f}".format(entree1Total)))
            print('%s. Entree1   ' % (newcount), appSpace(ManInventory.entree1), '@ $10.00: $%7s' % (entree1String))
        if ManInventory.entree2 !=0:
            count = count + 1
            newcount = str(count)
            entree2String = str(("{0:.2f}".format(entree2Total)))
            print('%s. Entree2   ' % (newcount), appSpace(ManInventory.entree2), '@ $12.50: $%7s' % (entree2String))
        if ManInventory.dessert !=0:
            count = count + 1
            newcount = str(count)
            dessertString = str(("{0:.2f}".format(dessertTotal)))
            print('%s. Dessert   ' % (newcount), appSpace(ManInventory.dessert), '@ $ 4.25: $%7s' % (dessertString))
        if ManInventory.dessert == 0 and ManInventory.entree1 == 0 and ManInventory.entree2 == 0 and ManInventory.salad == 0 and ManInventory.soup == 0 and ManInventory.appetizer == 0:
            print('No Items Sold             : $   0.00')

        print('                          :         ')
        print('Gross                     : $%7s' % (("{0:.2f}".format(subtotal))))
        print('Tax 8%%                    : $%7s' % (("{0:.2f}".format(tax8))))
        print('Register                  : $%7s' % (("{0:.2f}".format(totaltotal))))
        print('-' * 36)
        showLoop = 1

if __name__ == '__main__':
    Done = False
    MenuChoices = {}
    MenuChoices['S'] = 'Start New Order'
    MenuChoices['E'] = 'Edit Order'
    MenuChoices['P'] = 'Print Bill'
    MenuChoices['R'] = 'Receive Payment'
    MenuChoices['M'] = 'Manager Report'
    MenuChoices['Q'] = 'Quit'
    MenuOrder = ['S', 'E', 'P', 'R', 'M', 'Q']
    while not Done:
        print('')
        for letter in MenuOrder:
            print(letter, MenuChoices[letter])
        print('-----------------')
        choice = ' '
        while choice not in MenuChoices.keys():
                choice = input('Enter Choice> ')
                choice = choice.strip().upper()
                if not choice:
                    choice = ' '
        if choice == 'S':
            Show_Tables()
        if choice == 'E':
            Edit_Order()
        if choice == 'P':
            Print_Bill()
        if choice == 'R':
            Receive_Payment()
        if choice == 'M':
            Show_ManReport()
        if choice == 'Q':
            Done = True
