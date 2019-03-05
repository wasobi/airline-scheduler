# Sierra Obi
# CSC 110
# Fall 2015

def getChoice():
    # Displays all of the possible functions to the user
    # and asks the user for their choice. This is done until the
    # correct input is entered in by the user (i.e. an integer
    # beteen 1 - 8)

    print("")
    print(" Please specify your search criteria so we may assist you")
    print(" Enter a number that corresponds with one of the choices below:")
    print("      ---------------------------------------------------------")
    print("       1 - Search based on the name of the AIRLINE")
    print("       2 - Search based on the CHEAPEST FLIGHT available")
    print("       3 - Search based on a PRICE RANGE")
    print("       4 - Search based on the SHORTEST FLIGHT available")
    print("       5 - Search based on a DEPARTURE TIME RANGE")
    print("       6 - Search based on the AVERAGE PRICE for the")
    print("           desired airline")
    print("       7 - Search based on the name of the AIRLINE and")
    print("           the PRICE or DURATION")
    print("      ---------------------------------------------------------")
    print(" If you would like to QUIT >> Enter 8")
    choice = int(input("       Enter your selection: "))
    print("")
    # an integer 1 - 8 to represent the choices for the user
    return choice

def readFile():
    # Reads the selected file and strips the characters from the first line
    # then using a loop each line is stripped and stored in their designated
    # lists. The lines are split by te ',' and the prices are casted as
    # integers.

    airlines = []
    flightNumbers = []
    priceList = []
    depTimeList = []
    arrTimeList = []

    ## Get local variable for the file name used to open the file
    file = "airlines.txt"
    infile = open(file,'r')
    
    # Loop through the file  until each line is read and stored
    for line in infile:
        ## Strips the \n character from the end of the line each
        ## time the loop is iterated
        line.strip()
        ## separates the data in the current line in the file
        ## based on the placement of the comma
        airline, flightNumber, depTime, arrTime, price = line.split(",")

        ## updates the lists by adding the split data
        ## to each of the designated lists
        airlines = airlines + [airline]
        flightNumbers = flightNumbers + [flightNumber]
        depTimeList = depTimeList + [depTime]
        arrTimeList = arrTimeList + [arrTime]
        priceList = priceList + [(price)]
        
    infile.close()
        
    return airlines, flightNumbers, depTimeList, arrTimeList, priceList

def findAirline(name,airlines, flightNumbers, depList, arrList, prices):
    # The user will be prompted to enter the name of the airline of
    # their choosing until a valid entry is entered. The program will
    # then display all of the flights on the desired airline.

    while name not in airlines:
        print(" ")
        print("Not a valid airline name time. Please try again.")
        name = input("Enter the name of the airline service that you would like to use: ")
        
    savedIndex = 0
    indexes = []
    count = 0
    ## Searches for the name in the list of airlines
    for i in range(len(airlines)):
        if name == airlines[i]:
            ## Saves the index where the name is a match
            savedIndex = i
            ## Count is incremented each time a match is found
            count += 1
            ## The index is added to the list of indices
            indexes.append(savedIndex)

    print(" ")
    print("          -- Rhode Island Flight Finder AIRLINE SEARCH -- ")
    print(" ")

    ## Prints a table for each index where the name
    ## entered matches a name in the airline list
    if len(indexes) > 0:
        if count > 1:
            print("               There are",count," flights found for", name)
        else:
            print("                       There is 1 flight for", name)
        print(" ")
        ## Prints the table using the list of the saved indices
        ## from the airlines list and prints all of the
        ## corresponding information to that flight
        printTable(indexes,airlines, flightNumbers, depList, arrList, prices)

    ## Otherwise the user is informed that the name is not in the list
    else:
        print("                   Sorry, there were 0 flights found.")
        print("               Try another search or check the spelling.")
        
    return

def findCheapestFlight(airlines,flightNumbers,prices,priceList):
    # The flight with the lowest cost will be found and displayed
    # back to the user.
    lowPrice = prices[0]
    lowIndex = 0

    ## Searches element by element in the list and stores the
    ## index of the cheapest flight
    for i in range(len(prices)):
        if lowPrice > prices[i]:
            lowIndex = i

    print("        -- Rhode Island Flight Finder CHEAPEST PRICE SEARCH -- ")
    print(" ")

    ## Displays all of the corresponding flight info using the savend index
    ## of the lowest price
    print("                 ",airlines[lowIndex]," Flight Number",flightNumbers[lowIndex]," at",priceList[lowIndex])
    
    return lowIndex

def findPrice(priceThreshold,airlines,flightNumbers,depList,arrList,prices,priceList):
    # User is prompted to enter the maximum price desired.
    # Based on the maximum price that is entered the function
    # will find all flights with price that is lower than the price entered.
    # If no such price exists, the user will be prompted for another entry.
    # Otherwise a table of flights that are lower than the desired price
    # will be displayed.

    savedIndex = 0
    indexes = []
    count = 0

    lowIndex = lowestPrice(prices)

    ## Prompts the user for the a new price if the price returns
    ## nothing or 0
    while priceThreshold < prices[lowIndex]:
        print(" ")
        print(" Sorry, there were 0 flights found.")
        print(" The price you entered was too low. Try increasing your price.")
        print(" ")
        priceThreshold = int(input("Enter the maximum price of the flight you would like to take: "))
    
    ## Searches for the prices lower then the threshold in the list of prices
    for i in range(len(airlines)):
        if priceThreshold >= prices[i]:
            ## Saves the index where the price is less than or equal
            # to the threshold
            savedIndex = i
            ## Count is incremented each time a there is a price
            ## less than or equal to the threshold
            count += 1
            ## The index is added to the list of indices
            indexes.append(savedIndex)

    print(" ")
    print("           -- Rhode Island Flight Finder PRICE SEARCH -- ")
    print(" ")

    ## Prints a table for each index where the name
    ## entered matches a name in the airline list
    if len(indexes) > 0:
        if count > 1:
            print("           There are",count,"flights found at or below",priceThreshold,"USD")
        else:
            print("               There is 1 flight at or below",priceThreshold,"USD")
        print(" ")
        ## Prints the table using the list of the saved indices
        ## from the airlines list and prints all of the
        ## corresponding information to that flight
        printTable(indexes,airlines,flightNumbers,depList,arrList,priceList)
        
    return
 

def findShortestFlight(airlines,flightNumbers,depList,arrList):
    # The flight with the shortest time between the departure and the arrival
    # times will be found. This flight will then be displayed to the user.

    durations = []
    for i in range(len(depList)):
        duration = flightDuration(depList[i],arrList[i])
        durations = durations + [duration]

    shortestFlight = durations[0]
    shortIndex = 0
    ## Searches element by element in the list and stores the
    ## index of the shortest flight
    if (len(durations) > 0):
        for i in range(len(durations)):
            if durations[i]<shortestFlight:
                shortestFlight = durations[i]
                shortIndex = i

    print("       -- Rhode Island Flight Finder SHORTEST FLIGHT SEARCH -- ")
    print(" ")
    ## Displays all of the corresponding flight info using the savend index
    ## of the lowest price
    print("                     ",airlines[shortIndex]," Flight Number",flightNumbers[shortIndex])
    print("               departing at",depList[shortIndex],"and arriving at",arrList[shortIndex])
    print("                  Total Flight Duration:",durations[shortIndex],"minutes")

    return
    

def findDepartureTime(depMin,depMax,depTimes,airlines,flightNumbers,priceList,depList,arrList):
    # The user is asked for a minimum and maximum departure time.
    # Then the flight that is at least the minimun departure time and
    # and at the most the maximum departure time will be searched for.
    # All of the flights within this range will be displayed in a table.
    # If there is no such flight within this range then the user will
    # be prompted to raise their minimum.

    ## Variables for the index, a list of indices, the count, and the mimimum departure time
    savedIndex = 0
    indexes = []
    count = 0
    minTime = depTimes[0]
    
    ## Gets the hours and minutes from the departure and arrival lists
    ## and converts them to intergers (one for the hours and one for the minutes)
    depHour,depMinute = getFlightTime(depMin)
    minimum = (depHour * 60) + depMinute
    depHour,depMinute = getFlightTime(depMax)
    maximum = (depHour * 60) + depMinute
    
    ## Searches for the prices lower then the threshold in the list of prices
    for i in range(len(depTimes)):
        if depTimes[i] >= minimum and depTimes[i] <= maximum:
            ## Saves the index where the price is less than or equal
            ## to the threshold
            savedIndex = i
            ## Count is incremented each time a there is a price
            ## less than or equal to the threshold
            count += 1
            ## The index is added to the list of indices
            indexes.append(savedIndex)

        ## Keeps track of the minum
        if depTimes[i] < minTime:
            minTime = depTimes[i]
            earliest = depList[i]

    print(" ")
    print("        -- Rhode Island Flight Finder SEARCH BY DEPARTURE -- ")
    print(" ")

    ## Prints a table for each index where the name
    ## entered matches a name in the airline list
    if len(indexes) > 0:
        if count > 1:
            print("          There are",count,"flights found between",depMin,"and",depMax)
        else:
            print("                   There is 1 flight found between",depMin,"and",depMax)
        print(" ")
        ## Prints the table using the list of the saved indices
        ## from the airlines list and prints all of the
        ## corresponding information to that flight
        printTable(indexes,airlines,flightNumbers,depList,arrList,priceList)

    ## Otherwise the user is informed that the name is not in the list
    else: 
        print("            Sorry, there are 0 flights that depart at",depMin)
        print("             Please increase your mimimum departure time")
        print("                Earliest Departure from PVD >> MCO",earliest)
    
    return
   

def findAveragePrice(name,airlines,prices):
    # The user is prompted for the name of the airlines. Based on their input
    # the average flight price for the desired airline will be found.
    # If the airline entered is invalid, the user will be prompted until
    # a valid entry in received.

    ## Prompts the user for the re entry if the name of the airline
    ## is not found in the list of airlines
    while name not in airlines:
        print(" ")
        print("Not a valid airline name time. Please try again.")
        name = input("Ente the name of the airline service that you would like to use: ")

    priceSum = 0
    count = 0
    ## Searches for the name in the list of airlines
    for i in range(len(airlines)):
        if name == airlines[i]:
            ## If the airline is found at the index i, then
            ## the price corresponding to that flight is added
            ## to a sum
            priceSum += prices[i]
            count += 1
            
    ## The average is found for the sums
    averagePrice = priceSum/count

    print(" ")
    print("      -- Rhode Island Flight Finder SEARCH BY AVERAGE PRICE -- ")
    print(" ")
    print("             The average price for",name,"is",averagePrice,"USD.")
    
    return

def findAirlineSort(name,airlines,flightNumbers,depTimes,arrTimes,prices,depList,arrList,priceList):
    # The user will be prompted to enter the name of the airline of
    # their choosing until a valid entry is entered. The user is shown
    # the flights for the airline and they are prompted again whether
    # they would like to sort the flights by price or duration.
    # If the entry is invalid, the user will be prompted until they
    # enter in a correct choice for price or duration. The program will
    # then display all of the flights on the desired airline sorted based
    # on the choice of the user.

    while name not in airlines:
        print(" ")
        print("Not a valid airline name time. Please try again.")
        name = input("Enter the name of the airline service that you would like to use: ")
        
    savedIndex = 0
    savedIndexes = []
    count = 0
    airlineList = []
    sortedPrices = []
    durations = []
    #durationList = []
    ## Searches for the name in the list of airlines
    for i in range(len(airlines)):
        if name == airlines[i]:
            ## Saves the index where the name is a match
            savedIndex = i
            ## Count is incremented each time a match is found
            count += 1
            ## The index is added to the list of indices
            savedIndexes.append(savedIndex)

    ## Asks the user to choose how they would like to sort the flights
    sort = int(input("Enter the 1 if you would like to sort by PRICE and 2 for FLIGHT DURATION:"))


    print(" ")
    print("          -- Rhode Island Flight Finder AIRLINE SEARCH -- ")
    print(" ")

    ## Sorts the lists and prints out the table based on the user input
    if len(savedIndexes) > 0:
        if sort == 1:
            if count > 1:
                print("               There are",count," flights found for", name)
            else:
                print("                       There is 1 flight for", name)
            print(" ")
            ## Prints the table using the list of the saved indices
            ## from the airlines list and prints all of the
            ## corresponding information to that flight
            printTable(savedIndexes,airlines, flightNumbers, depList, arrList, priceList)
                       
        elif sort == 2:
            ## creates a list of durations based off of the saved indexes                      
            for k in range(len(savedIndexes)):
                duration = flightDuration(depList[savedIndexes[k]],arrList[savedIndexes[k]])
                durations = durations + [duration]

            sortedDurations,savedIndexes = insertionSort(durations,savedIndexes)

            if count > 1:
                print("               There are",count," flights found for", name)
            else:
                print("                       There is 1 flight for", name)
            print(" ")
            ## Prints the table using the list of the saved indices
            ## from the airlines list and prints all of the
            ## corresponding information to that flight
            printTable(savedIndexes,airlines, flightNumbers, depList, arrList, priceList)
            
        else:
            print("Not a valid option, please try again.")
            sort = int(input("Enter the 1 if you would like to sort by PRICE and 2 for FLIGHT DURATION:"))

    else:
        print("                   Sorry, there were 0 flights found.")
        print("               Try another search or check the spelling.")
    
    return

def convertPrices(priceList):
    # Converts a list of string into integers to represent
    # the prices for each of the flights
    prices = []
    for i in range(len(priceList)):
        price = priceList[i]
        price = price[1:]
        prices = prices + [int(price)]
    return prices

def convertFlightTimes(depList,arrList):
    # Converts the flight time from 24:00 format to
    # a minute format element by element in the list
    depTimes =[]
    arrTimes =[]
    for i in range(len(depList)):
        depHour,depMin = getFlightTime(depList[i])
        depTime = (depHour * 60) + depMin
        depTimes = depTimes + [depTime]
    for i in range(len(arrList)):
        arrHour,arrMin = getFlightTime(arrList[i])
        arrTime = (arrHour * 60) + arrMin
        arrTimes = arrTimes + [arrTime]
        
    return depTimes,arrTimes

def flightDuration(departures,arrivals):
    # This function receives the departure and the arrival of a flight.
    # Based on the 24:00 clock format, the function will calculated
    # the duration of the flight and return the amount in minutes.

    ## Defines the number of minutes in a full day
    day = 1440

    ## Getting the hours and minutes from the departure and arrival times
    depHour,depMin = getFlightTime(departures)
    arrHour,arrMin = getFlightTime(arrivals)

    ## Multiplies the int representing the hour by 60
    ## to convert the hour into minutes then adds
    ## the additonal minutes
    depTime = (depHour * 60) + depMin
    arrTime = (arrHour * 60) + arrMin
    
    if (depTime < day):
        duration =  abs(depTime - arrTime)
    else:
        arrTime =  arrTime + day
        duration =  abs(depTime - arrTime)
        
    return duration

def getFlightTime(flightTime):
    # Receives a string that holds the flight time a 24 hour
    # format. The colon is removed from the string and the
    # hour and minutes from that string are returned.
    hour,minute = flightTime.split(":")
    hour = int(hour)
    minute = int(minute)
    
    return hour,minute

def lowestPrice(prices):
    # Finds the lowest price in a list of prices. These prices must be
    # Given in the form of a list and must be intergers or floats.
    
    lowPrice = prices[0]
    index = 0
    ## Finds the lowest price in the list and saves the index
    for i in range(len(prices)):
        if lowPrice > prices[i]:
            index = i
    return index

def insertionSort(theList,savedIndexes):
    # The partion begins at the beginning of the list and is incremented
    # by 1 each time. The left of the partition is always considered to
    # be sorted.

    #print(savedIndexes)
    #print(theList)
    
    for i in range(1, len(theList)):
        save1 = theList[i]
        save2 = savedIndexes[i]
        j = i
        while j > 0 and theList[j - 1] > save1:
            ## comparison
            theList[j] = theList[j - 1]
            j = j - 1
	    ## swap
        theList[j] = save1
        savedIndexes[j] = save2

    print(savedIndexes)
    print(theList)
        
    return theList,savedIndexes

def printTable(indexes,airlines,flightNumbers,depTimes,arrTimes,prices):
    # Prints a table of the complete information of an airline.
    print("             AIRLINE","\t","FLT#","\t","DEPT","\t","ARVL","\t","PRICE")
    print("            __________________________________________")
    print(" ")
    
    for i in range(len(indexes)):
        print("             ",airlines[indexes[i]],"\t",flightNumbers[indexes[i]],"\t",depTimes[indexes[i]],"\t",arrTimes[indexes[i]],"\t ",prices[indexes[i]])
    return
    
def main():
    # The main function will implement the corresponding choice selection to
    # the correct function. If 8 is selected, the program will say goodbye
    # and the program will stop running.

    print(" ---------------------------------------------------------------- ")
    print("|                     Rhode Island Flight Finder                 |")
    print(" ---------------------------------------------------------------- ")
    print(" ")

    ## Extracts the data from the file
    airlines,flightNumbers,depList,arrList,priceList = readFile()

    ## Converts the prices to a list of integers for computations
    prices = convertPrices(priceList)

    ## Converts the flight times into minutes (list of integers) for computations
    depTimes,arrTimes = convertFlightTimes(depList,arrList)

    ## Asks the user for their choice
    userChoice = getChoice()
    
    while userChoice != 8:
         
        if userChoice == 1:
            name = input("Ente the name of the airline service that you would like to use: ")
            findAirline(name,airlines,flightNumbers,depList,arrList,priceList)

            print("")
            
            userChoice = getChoice()
            
        elif userChoice == 2:
            findCheapestFlight(airlines,flightNumbers,prices,priceList)
            userChoice = getChoice()

            print("")
            
        elif userChoice == 3:
            maxPrice = int(input("Ente the maximum price that you would like your flight to be: "))
            findPrice(maxPrice,airlines,flightNumbers,depList,arrList,prices,priceList)
            userChoice = getChoice()

            print("")
            
        elif userChoice == 4:
            findShortestFlight(airlines,flightNumbers,depList,arrList)
            userChoice = getChoice()

            print("")
            
        elif userChoice == 5:
            print("Please enter the following in 24:00 time format >>")
            print("")

            ## Prompts the user for a valid departure time until it is entered
            depMin = input("Enter the minimum departure time: ")
            while ':' not in depMin:
                print("Not a valid departure time. Please try again.")
                depMin = input("Enter the minimum departure time: ")

            ## Prompts the user for a valid arrival time until it is entered
            depMax = input("Enter the maximum departure time: ")
            while ':' not in depMax:
                print("Not a valid departure time. Please try again.")
                depMax = input("Enter the minimum departure time: ")
            
            findDepartureTime(depMin,depMax,depTimes,airlines,flightNumbers,priceList,depList,arrList)
            userChoice = getChoice()

            print("")
            
        elif userChoice == 6:
            name = input("Ente the name of the airline service: ")
            findAveragePrice(name,airlines,prices)
            userChoice = getChoice()

            print(" ")

        elif userChoice == 7:
            name = input("Ente the name of the airline service that you would like to use: ")
            findAirlineSort(name,airlines,flightNumbers,depTimes,arrTimes,prices,depList,arrList,priceList)
            userChoice = getChoice()

            print("")
            
        else:
            print("Please enter in a valid value that\nrepresents one of the previous values.")
            userChoice = int(input(" Enter your selection: "))
            
            print("")
            
    print("Thank you for using the Rhode Island Flight Finder >>")
    

main()
