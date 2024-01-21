#!/usr/bin/python
import pandas as pd
import utils as ut

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
    
    picks = [[]]
    losers = []
    n = 0
    #I can make it all a big loop. Oh no.
    while n == 0 or len(set(picks[n])) > 2:
        n += 1

        #Find the picks
        picks.append([0]*cols)
        for index, row in data.iterrows():
            row = list(row)
            minVote = 1
            while row.index(minVote) in losers:
                minVote += 1
            picks[n][row.index(minVote)] += 1
        
        #Do the loser(s)
        [losers.append(x) for x in ut.indexes(picks[n], ut.minNonZero(picks[n]))]

    [print(data.columns[x]) for x in ut.indexes(picks[n], max(picks[n]))]

if __name__ == "__main__":
    main()