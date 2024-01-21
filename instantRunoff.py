#!/usr/bin/python
import pandas as pd
import indexes as ind

#Function to check if an array has duplicate numbers in the rows
def checker(data):
    isOk = True
    for index, row in data.iterrows():
        values = []
        for i in row:
            if i in values:
                isOk = False
                print("Row ", index, " has a duplicate.")
            else:
                values.append(i)
    return isOk

def main():
    array = "IndustrialRevolution.csv" #Insert filepath of csv as a string to array
    data = pd.read_csv(array)
    cols = len(data.columns)

    #Just a quick sanity check
    if checker(data) == False:
        print("This CSV has duplicates in the rows. Fix it!")
        return 1
    
    #Find the first picks
    firstPicks = [0]*cols    
    for index, row in data.iterrows():
        row = list(row)
        firstPicks[row.index(1)] += 1
    
    #Set up and do the first round's loser(s)
    losers = []
    [losers.append(x) for x in ind.indexes(firstPicks, min(firstPicks))]

    #Second round time
    secondPicks = [0]*cols
    for index, row in data.iterrows():
        row = list(row)
        minVote = 1
        while row.index(minVote) in losers:
            minVote += 1
        secondPicks[row.index(minVote)] += 1
    print(secondPicks)


if __name__ == "__main__":
    main()