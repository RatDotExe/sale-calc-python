from decimal import *
import math
again = "y"
while again == "y":
    op = raw_input("What's the original price? ")
    sp = raw_input("What's the sale %? ")

    spnum = Decimal(sp)
    opnum = Decimal(op)
    spnum2 = spnum / 100

    perc = 1 - spnum2

    r = opnum * perc

    print r
    print ("Would you like to do another calculation? ")
    again = raw_input("y for yes or n for no: ")