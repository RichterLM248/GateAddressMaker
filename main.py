#Written by RichterLM248
#January 2022

import random

userInp = ""

gateString = ""

gatefile = open('gateadrs.txt', 'r') #.txt file of gate addresses, one per line

while(userInp != "q"):

    userInp = input("Enter how many addresses you want, or q to quit: ")

    #Gate address is 8 digits, 1 - 14, seperated by -
    #TODO: Check against current existing list and add addresses to the list

    for x in range(int(userInp)):

        gateString = ""
        lcv = 0
        for lcv in range(8):
            gateString += str(random.randint(1,14))

            if lcv < 7:
                gateString += "-"

        #TODO: check gateString against contents of gateadrs
        filelines = gatefile.readlines()

        for line in filelines:

            #print("LINE IS: " + line)
            #print("GATESTRING IS: " + gateString)

            while line == gateString:

                for lcv in range(8):

                    gateString += str(random.randint(1, 14))

                    if lcv < 7:
                        gateString += "-"
        print(gateString)

