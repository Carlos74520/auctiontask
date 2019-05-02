''' An auction company has an interactive auction board at their sales rooms, which
allows buyers to place bids at any time during the auction. Before the auction starts, the sellers
place their items in the sale room with a unique number attached to each item (item number).
The following details about each item need to be set up on the interactive auction board system:
item number, number of bids, description and reserve price. The number of bids is initially set to zero.

During the auction, buyers can look at the items in the sale room and then place a bid on the interactive
auction board at the sale room. Each buyer is given a unique number for identification (buyer number).
All the buyer needs to do is enter their buyer number, the item number and their bid. Their bid must be greater than any existing bids.

At the end of the auction, the company checks all the items and marks those that have bids greater than the reserve as sold.
Any items sold will incur a fee of 10% of the final bid to be pad to the auction company. 

Write and test a program of programs for the auction company. 

- Your program or programs must include appropriate prompts for the entry of data, data must be validated on entry. 
- Error messages and other input need to be set out clearly and understandably. 
- All variables, constants and other identifiers must have meaningful names. 

You will have to complete these three tasks. Each must be fully tested. 

Task 1 - Auction set up. 

For every item in the auction the item number, description and the reserve price should be recorded. 
The number of bids is set to zero. There must be at least 10 items in the auction. 

Task 2 - Buyer bids. 

A buyer should be able to find an item and view the item number, description and the current highest bid. A buyer
can then enter their buyer number and bid, which must be higher than any previously recorded bids. Every time a bid 
is recorded the number of bids for that item is increased by one. Buyers can bid for an item many times and they 
can bid for many items. 

Task 3 - At the end of the auction. 

Using the results from Task 2, identify items that have reached their reserve price, mark them as sold, calculate 
10% of the final bid as the auction company fee and add this to the total fee for all sold items. Display this total fee.
Display the item number and final bid for all the items with bids that have not reached their reserve
price. Display the item number of any items that have received no bids. Display the number of items sold, the 
number of items that did not meet the reserve price and the number of items with no bids. 
'''

#YOU CANT INPUT NEGATIVE NUMBERS
#declare variables
auctionlist = []
buyerlist= []
itemnumber = 0
buyeradd = True
buyerarray = []
buyertemp = []
counter = -1
bidding = False
bidprocess = True
templastbid = float(0)
processing = True
avoiduselessquestioncounter = 0
testnumber = 0
totalfee = 0
salescounter = 0
buyernamepick = ''
registeredbuyers = []
buyerboolean = True

#makes sure that its an integer and doesnt break the code (9 times out of 10 thats why theres a 'while true' loop)
#make sure you cant input -1
while True:
    try:
        itemamount = int(input('\n how many items are there to auction?     '))
        if itemamount > 0 : #and itemamount >= 10
            break
        else:
            print('\n you cannot input numbers smaller than 1')
    except ValueError:
        print('\n incorrect notation, you must input an integer')
    
#this makes innitial item list for bidders to see
for i in range(itemamount):
    itemindividual = []
    itemnumber += 1
    print('\n FOR ITEM NUMBER', itemnumber, ':')
    intemdescription = input('\n what is the item?   ')
    while True:
        try:
            reserveprice = float(input('\n what is the reserve price?     '))
            break
        except ValueError:
            print('\n incorrect notation')
#append individual factors into the temporary 1D array
    itemindividual.append(itemnumber) #index 0
    itemindividual.append(intemdescription) #index 1
    itemindividual.append(0) #<-- number of bids #index 2
    itemindividual.append(reserveprice) #index 3
    itemindividual.append(0) #<-- this is the current highest bid #index 4
    itemindividual.append(0) #<-- this is to get replaced with the buyerarray #index 5
#appends the 1D array into the other 1D array, making it a easier to use 2D array
    auctionlist.append(itemindividual)



#this makes an array for bidders so that I can append to them later on
while buyeradd:
    while True:
        try:
            buyernumber = int(input('\n how many buyers are there?     '))
        except ValueError:
            print('\n incorrect notation')
        if buyernumber > 0:
            break
        else:
            print('\n please input a value bigger than 0')
    for i in range(buyernumber):
        buyerlist.append([i+1])
    buyeradd = False


bidding = True
def showlist():
    print('\n here are the current items and their information:')
    print('\n | ID: | ITEM DESCRIPTION: | CURRENT BID')
    for i in range(itemamount):
        print(' |', auctionlist[i][0], '  |', auctionlist[i][1], ' '* (16 - len(auctionlist[i][1])), '|', auctionlist[i][4])


bidding = True
print('\nAUCTION STARTING')
while bidding:
    print('\n', '_'*40)
    showlist()
    processing = True
    bidprocess = True
    if avoiduselessquestioncounter > 0:
        buyerboolean = True
        while True:
            try:
                    testnumber = 0
                    auctionquestion = input('\n are there more bids coming in? (y/n)   ')
                    if auctionquestion == 'y':
                        break
                    elif auctionquestion == 'n':
                        testnumber = 1
                        bidding = False
                        break
                    else:
                        print('\n incorrect input notation')
            except:
                print('\n how did you even get here')
    if bidding == False:
        break
    while True:
        try:
            buyeridpick = int(input('\n please enter buyer id    '))
            if buyeridpick <= len(buyerlist) and buyeridpick > 0:
                break
            else:
                print('\n This ID does not exist')
        except ValueError:
            print('\n you inputed incorrect notation. Make sure it is an integer')
    if len(registeredbuyers) > 0:
        for i in range(len(registeredbuyers)):
            if registeredbuyers[i] in buyerlist[buyeridpick - 1]:
                print('\n welcome back', buyerlist[buyeridpick - 1][1])
                buyernamepick = buyerlist[buyeridpick -1][1]
                buyerboolean = False
        if buyerboolean == True:
            buyernamepick = input('\n please input your name    ')
            registeredbuyers.append(buyeridpick)
            buyerlist[buyeridpick - 1].append(buyernamepick)
    else:
        buyernamepick = input('\n please input your name    ')
        registeredbuyers.append(buyeridpick)
        buyerlist[buyeridpick - 1].append(buyernamepick)
    while True:
        try:
            itemchoice = int(input('\n what item number do you want to bid on?     '))
            if itemchoice > 0 and itemchoice <= len(auctionlist):
                break
            else:
                print('\n that is not an item that is in the provided list')
        except ValueError:
            print('\n that is invalid notation, please input an integer')
    counter = -1
    while processing:
        counter += 1
        while bidprocess:
            if auctionlist[counter][0] == itemchoice:
                print('\n the current highest bid for the', auctionlist[counter][1], 'is', auctionlist[counter][4])
                while True:
                    try:
                        bidamount = float(input('\n how much are you bidding?     '))
                        break
                    except ValueError:
                        print('\n Invalid notation, please input a number')
                if bidamount > auctionlist[counter][4]: #<-- auctionlist[counter] is the current highest bid
                    auctionlist[counter][4] = bidamount #<-- that changes the current bid
                    buyerarray.append(buyeridpick)
                    buyerarray.append(buyernamepick)
                    auctionlist[counter][5] = buyerarray
                    auctionlist[counter][2] += 1
                    buyerarray = []
                    avoiduselessquestioncounter += 1
                    processing = False
                    bidprocess = False
                    bidding =  True
                    break
                else:
                    while True:
                        try:
                            choice = input('\n the amount you bidded is lower that the current bid, would you like to cancel bid or re-add another value? (add/cancel)     ')
                            if choice == 'add' or choice == 'cancel':
                                break
                            else:
                                print("\n incorrect notation")
                        except:
                            print('\n How did you even reach here')
                    if choice == 'cancel':
                        buyerarray = []
                        processing = False
                        bidprocess = False
                        break
            else:
                break
        else:
            break
print('_'*40)
print('\n AUCTION ENDED')
counter = 0 #reset counter
for i in range(len(auctionlist)):
    if auctionlist[i][4] > auctionlist[i][3]: #checks if the bid amount is bigger than reserve price
        auctionlist[i].append(True) #index 6
        salescounter += 1
    else:
        auctionlist[i].append(False) #still index 6
for i in range(len(auctionlist)):
    if auctionlist[i][6] == True:
        auctionlist[i].append(auctionlist[i][4] * 0.1)  #appends the 10% fee needed #index 7
        auctionlist[i].append(auctionlist[i][4] * 1.1)  #this is the full price to pay #index 8
for i in range(len(auctionlist)): #tests for unsuccessful sales
    if auctionlist[i][6] != True:
        counter += 1
    if counter == len(auctionlist): 
        print('there were no successful sales') #to avoid printing a useless message
    if auctionlist[i][6] == True:
        print('\n successful bids and bidders are:')
        print('\n', auctionlist[i][5][1], '(buyer id', auctionlist[i][5][0], ') buying the:', auctionlist[i][1], 'at the price of:  $', str(round(auctionlist[i][8], 2)), 'fee included')
        totalfee += auctionlist[i][7]
        totalfee = round(totalfee, 2)
if salescounter != len(auctionlist):
    print('\n unsuccessfull sales where:')
    for i in range(len(auctionlist)):
        if auctionlist[i][6] == False:
            print('\n', auctionlist[i][1], '(item number', auctionlist[i][0], ') which did not meet its reserve price of $', auctionlist[i][3])
else:
    print('\n there were no unsuccessful sales')
counter = 0 #reset counter
for i in range(len(auctionlist)):
    #tests if there are indeed bids in that one, if there is, adds to a counter
    if auctionlist[i][2] != 0: 
        counter += 1
    if counter == len(auctionlist): #if the counter is the same as the amount of items, then every item must at least have one bid in them
        print('\n every item recieved a bid')
        break
    if i == len(auctionlist) and counter < len(auctionlist):
        print('\n There were no bids on:')
        if auctionlist[i][2] == 0:
            print('\n', auctionlist[i][1], 'item number:', auctionlist[i][0])
if salescounter > 1 and len(auctionlist) - salescounter > 1:
    print('\n there are', salescounter, 'items who have been sold and', len(auctionlist) - salescounter, 'items that have not being sold as they did not reach their reserve price')
elif salescounter > 1 and len(auctionlist) - salescounter == 1:
    print('\n there are', salescounter, 'items who have been sold and', len(auctionlist) - salescounter, 'item that has not been sold as it did not reach its reserve price')
elif salescounter == 1 and len(auctionlist) - salescounter > 1:
    print('\n there is only', salescounter, 'item that has been sold and', len(auctionlist) - salescounter, 'items that have not being sold as they did not reach their reserve price')
elif salescounter == 0:
    print('\n no items got sold, so all items did not reach their reserve price')
elif len(auctionlist) - salescounter == 0:
    print('\n all items have successfully been sold')
else:
        print('\n there is only', salescounter, 'item that has been sold and', len(auctionlist) - salescounter, 'item that has not been sold as it did not reach its reserve price')
print('\n total fee is: $', totalfee) #prints total fee
print('_'*40)
