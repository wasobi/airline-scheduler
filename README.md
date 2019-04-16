# airline-scheduler

## Project Overview
A mini-python program that shows flights from Providence to Orlando.

## General Solution

 A function will read the data in from the file and store the
 information present in an empty list designated for that piece of
 data. The lists with the flight data will be returned an used later.
 Use loops to prompt the user for a choice until they choose
 to exit the program. Create a function that gets the choice from the user
 then execute the correct function to find the flight based on the
 specifications from the user. Based on the selection, the flights that
 match the search criteria will be returned to the user in an organized
 form (i.e. a table or a single print statement). The input will be matched
 to the items in one of the list and the index or indices that match
 that input will be saved. Using this index, complete flight information
 will be pulled from each of the other lists by matching the indices from
 the list we first used to search for the data to a corresponding list
 that contains another portion of the original flight data.

## Pseudocode

```python
 User is prompted to enter the name of the file
 The user is prompted for their choice (1-8)
 While the choice is not 8
       if choice is 1
           prompt for airline
           find the flights based off of the airline
       if choice is 2
           find the cheapest flight
       if choice is 3
           prompt for price
           find the flights under the maximum price
       if choice is 4
           find shortest flight
       if choice is 5
           prompt for departure and arrival times
           find flights betweenthe range
       if choice is 6
           prompt for the airline
           find the average flight price for that airline
       if choice is 7
           prompt for airline and display flights
           prompt for choice of sorting (price or duration)
           sort the flights based on choice
  Otherwise "Goodbye" is displayed
```
